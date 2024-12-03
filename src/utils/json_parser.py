import json
import logging

from structure.winter_supplement import WinterSupplementInput


logger = logging.getLogger(__name__)


def read_winter_supplement_input(input_json_str: str) -> WinterSupplementInput:
    """
    read a json string and turn it into WinterSupplementInput
    """
    json_dict = json.loads(input_json_str)
    logger.debug(f"Got input_json_str: \n{input_json_str}")
    return WinterSupplementInput.new_one_from_dict(json_dict)
