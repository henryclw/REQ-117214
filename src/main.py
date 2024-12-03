import argparse
import logging
import os
import paho.mqtt.client as mqtt

from message_queue.mqtt_connection import MqttConnection
from utils.config_helper import BasicConfig


logger = logging.getLogger(__name__)


if __name__ == "__main__":

    # the args for command line
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="This program is designed to solve the written assignment of the REQ117214",
        epilog=""
    )
    parser.add_argument("--log",
                        help="the logging level of this program, the default level is INFO", default="INFO")
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

    # setting up logging configs, the logging level is from command line args
    numeric_level = getattr(logging, args.log, None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % args.log)
    logging.basicConfig(level=numeric_level,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")

    logger.info(f"Program started with mqtt_topic_id: {basic_config.mqtt_topic_id}")
    logger.info(f"Going to connect MQTT at host {basic_config.mqtt_hostname} with port {basic_config.mqtt_port}")

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_connection = MqttConnection(topic_id=basic_config.mqtt_topic_id)
    mqtt_client.on_connect = mqtt_connection.on_connect
    mqtt_client.on_message = mqtt_connection.on_message
    mqtt_client.on_subscribe = mqtt_connection.on_subscribe
    mqtt_client.on_unsubscribe = mqtt_connection.on_unsubscribe

    mqtt_client.connect(basic_config.mqtt_hostname, basic_config.mqtt_port, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    mqtt_client.loop_forever()
