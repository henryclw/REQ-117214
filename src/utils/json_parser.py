import json

from structures.winter_supplement import WinterSupplementInput


def read_winter_supplement_input(input_json_str: str) -> WinterSupplementInput:
    json_dict = json.loads(input_json_str)
    print(json_dict)
    # return WinterSupplementInput(**json_dict)
    return WinterSupplementInput.new_one_from_dict(json_dict)
