import logging

import paho.mqtt.client as mqtt

from engine.rule_engine import calculate_eligible_supplement
from utils.json_parser import read_winter_supplement_input

logger = logging.getLogger(__name__)


class MqttConnection:
    def __init__(self, topic_id):
        self.topic_id = topic_id


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("BRE/calculateWinterSupplementInput/" + self.topic_id)
        logger.info("subscribed " + "BRE/calculateWinterSupplementInput/" + self.topic_id)
        # client.subscribe("#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        logger.info(f"Got payload from topic: {msg.topic}\n{msg.payload}")

        winter_supplement_input = read_winter_supplement_input(msg.payload)
        logger.debug(f"Parsed winter_supplement_input: {winter_supplement_input}")
        output = calculate_eligible_supplement(winter_supplement_input)
        logger.info(f"calculate result: {output}")
        publish_info = client.publish(topic=f"BRE/calculateWinterSupplementOutput/{self.topic_id}", payload=output.get_json_str(), qos=1)
        logger.info(f"try publishing {output.get_json_str()} into BRE/calculateWinterSupplementOutput/{self.topic_id}")
        # publish_info.wait_for_publish()
        logger.info(f"published payload into calculateWinterSupplementOutput")

    def on_subscribe(self, client, userdata, mid, reason_code_list, properties):
        # Since we subscribed only for a single channel, reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            logger.info(f"Broker rejected you subscription: {reason_code_list[0]}")
        else:
            logger.info(f"Broker granted the following QoS: {reason_code_list[0].value}")

    def on_unsubscribe(self, client, userdata, mid, reason_code_list, properties):
        # Be careful, the reason_code_list is only present in MQTTv5.
        # In MQTTv3 it will always be empty
        if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
            logger.info("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
        else:
            logger.info(f"Broker replied with failure: {reason_code_list[0]}")
        client.disconnect()
