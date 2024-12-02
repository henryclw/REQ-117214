import logging
import paho.mqtt.client as mqtt
import time


logger = logging.getLogger(__name__)


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        logger.info(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        logger.info(f"Broker granted the following QoS: {reason_code_list[0].value}")


def on_message(client, userdata, msg):
    if "WinterSupplement" in msg.topic:
        logger.info(f"Got result from topic: {msg.topic}\n{msg.payload}")


def on_connect(client, userdata, flags, reason_code, properties):
    logger.info("Connected with result code " + str(reason_code))


def read_example_list():
    with open("../test/test_parser_examples/good_010_input.json") as f:
        json_str = f.read()
    return [json_str]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")
    logger.info("Started mock web script")
    logger.info("This script is an alternative as the testing web app. It behaves like the web app, " +
                "it sends the input data to calculateWinterSupplementInput, " +
                "and read the output data from rule engine from calculateWinterSupplementOutput.")
    logger.info("Please make sure that the main server is running before testing with this script.")
    logger.info("If set up properly, you should expect some corresponding calculation result from " +
                "the topic calculateWinterSupplementOutput.")

    example_list = read_example_list()

    topic_id = "f04fd7e0-15d1-4c61-adc9-433e67ae527c"

    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_subscribe = on_subscribe

    mqttc.connect("test.mosquitto.org", 1883, 60)
    mqttc.loop_start()
    mqttc.subscribe(f"BRE/calculateWinterSupplementOutput/{topic_id}")
    logger.info(f"Try subscribing BRE/calculateWinterSupplementOutput/{topic_id}")
    time.sleep(3)
    for example_input in example_list:
        publish_info = mqttc.publish(f"BRE/calculateWinterSupplementInput/{topic_id}", example_input)
        logger.info(f"try publishing {example_input} into BRE/calculateWinterSupplementInput/{topic_id}")
        publish_info.wait_for_publish()
        logger.info(f"published payload into BRE/calculateWinterSupplementInput/{topic_id}")

    time.sleep(60)
    mqttc.loop_stop()
    logger.info("Ended mock web script")
