import argparse
import glob
import logging
import os
import paho.mqtt.client as mqtt
import time

from typing import List
from utils.config_helper import BasicConfig

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
    logger.info("Connected to MQTT server with result code " + str(reason_code))


def read_example_list() -> List[str]:
    all_filenames = glob.glob("test/test_parser_examples/good_input_*.json")
    all_json_str = []
    for filename in all_filenames:
        with open(filename) as f:
            all_json_str.append(f.read())
    return all_json_str


if __name__ == "__main__":
    script_description = """
    This script is an alternative as the testing web app. It behaves like the web app, it sends the input data to 
    calculateWinterSupplementInput, and read the output data from rule engine from calculateWinterSupplementOutput.
    Please make sure that the main server is running before testing with this script.
    If set up properly, it could show the corresponding calculation results from topic calculateWinterSupplementOutput.
    """
    parser = argparse.ArgumentParser(
        prog="mock_web_app.py",
        description=script_description,
        epilog=""
    )

    parser.add_argument("--mqtt_topic_id",
                        help="the topic id of mqtt, this could be the unique ID from the web calculator",
                        default=os.getenv("MQTT_TOPIC_ID", "NULL"))
    parser.add_argument("--mqtt_hostname",
                        help="the hostname of the mqtt connection",
                        default=os.getenv("MQTT_HOSTNAME", default="test.mosquitto.org"))
    parser.add_argument("--mqtt_port",
                        help="the port of the mqtt connection",
                        default=int(os.getenv("MQTT_PORT", default=1883)))
    args = parser.parse_args()
    BasicConfig.set_config_from_args(args)
    basic_config = BasicConfig.get_config()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")
    logger.info("Started mock web script")
    logger.info(script_description)

    example_list = read_example_list()

    topic_id = basic_config.mqtt_topic_id

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.on_subscribe = on_subscribe

    mqtt_client.connect(basic_config.mqtt_hostname, basic_config.mqtt_port, 60)

    mqtt_client.loop_start()
    mqtt_client.subscribe(f"BRE/calculateWinterSupplementOutput/{topic_id}")
    logger.info(f"Try subscribing BRE/calculateWinterSupplementOutput/{topic_id}")
    time.sleep(3)
    for example_input in example_list:
        publish_info = mqtt_client.publish(f"BRE/calculateWinterSupplementInput/{topic_id}", example_input)
        logger.debug(f"try publishing payload into BRE/calculateWinterSupplementInput/{topic_id}")
        publish_info.wait_for_publish()
        logger.info(f"published payload {example_input} into BRE/calculateWinterSupplementInput/{topic_id}")
        time.sleep(5)

    mqtt_client.loop_stop()
    logger.info("Ended mock web script")
