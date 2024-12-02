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
        logger.info(f"Got payload from topic: {msg.topic}\n{msg.payload}")


def on_connect(client, userdata, flags, reason_code, properties):
    logger.info("Connected with result code " + str(reason_code))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")
    logger.info("Started mock web script")
    logger.info("This script is an alternative as the testing web app. It behaves like the web app, it sends the " +
                "input data to certain topic, and read the output data from rule engine from the topic.")

    topic_id = "f04fd7e0-15d1-4c61-adc9-433e67ae527a"

    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_subscribe = on_subscribe

    mqttc.connect("test.mosquitto.org", 1883, 60)
    mqttc.loop_start()
    mqttc.subscribe("#")
    logger.info("Subscribed")
    time.sleep(3)
    for i in range(3):
        publish_info = mqttc.publish(f"BRE/calculateWinterSupplementInput/{topic_id}", f"a string {i}")

        logger.info(f"try publishing")
        publish_info.wait_for_publish()
        logger.info(f"published payload into calculateWinterSupplementInput")

    time.sleep(30)
    mqttc.loop_stop()
    logger.info("Ended mock web script")
