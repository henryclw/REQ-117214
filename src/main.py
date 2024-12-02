import argparse
import logging
import paho.mqtt.client as mqtt

from engine.rule_engine import calculate_eligible_supplement
from message_queue.mqtt_connection import MqttConnection
from utils.json_parser import read_winter_supplement_input


logger = logging.getLogger(__name__)


if __name__ == "__main__":

    # the args for command line
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="This program is designed to solve the written assignment of the REQ117214",
        epilog=""
    )
    parser.add_argument("--log", help="the logging level of this program, the default level is INFO", default="INFO")
    args = parser.parse_args()

    # setting up logging configs, the logging level is from command line args
    numeric_level = getattr(logging, args.log, None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % args.log)
    logging.basicConfig(level=numeric_level,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")

    with open("./test/test_parser_examples/good_010_input.json") as f:
        json_str = f.read()
        winter_supplement_input = read_winter_supplement_input(json_str)
        logger.debug(f"Read winter_supplement_input: {winter_supplement_input}")
        output = calculate_eligible_supplement(winter_supplement_input)
        logger.info(f"calculate result: {output}")

    logger.info("--------------------")
    topic_id = "f04fd7e0-15d1-4c61-adc9-433e67ae527c"
    logger.info(f"topic id is {topic_id}")

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_connection = MqttConnection(topic_id="f04fd7e0-15d1-4c61-adc9-433e67ae527c")
    mqtt_client.on_connect = mqtt_connection.on_connect
    mqtt_client.on_message = mqtt_connection.on_message
    mqtt_client.on_subscribe = mqtt_connection.on_subscribe
    mqtt_client.on_unsubscribe = mqtt_connection.on_unsubscribe

    mqtt_client.connect("test.mosquitto.org", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    mqtt_client.loop_forever()
