from dataclasses import dataclass


@dataclass
class ConfigHolder:
    mqtt_topic_id: str
    mqtt_hostname: str
    mqtt_port: int


class BasicConfig:
    _inner_config: ConfigHolder = None

    @staticmethod
    def set_config_from_args(args):
        if args.mqtt_topic_id == "NULL":
            raise ValueError("MQTT topic id is never set, " +
                             "please set it either using command line args or environment variable")
        BasicConfig._inner_config = ConfigHolder(
            mqtt_topic_id=args.mqtt_topic_id,
            mqtt_hostname=args.mqtt_hostname,
            mqtt_port=args.mqtt_port,
        )

    @staticmethod
    def get_config() -> ConfigHolder:
        if BasicConfig._inner_config is None:
            raise ValueError("Basic config is never set")
        return BasicConfig._inner_config
