import json
import re

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


# familyComposition could only be single or couple
class FamilyCompositionType(Enum):
    SINGLE = "single"
    COUPLE = "couple"


@dataclass
class WinterSupplementInput:
    id: str
    number_of_children: int
    family_composition: FamilyCompositionType
    family_unit_in_pay_for_december: bool

    @staticmethod
    def new_one_from_dict(input_dict) -> Optional["WinterSupplementInput"]:

        # make sure that every key is in the input data
        if "id" not in input_dict:
            raise KeyError(f"Could not find key id in input data: {input_dict}")
        if "numberOfChildren" not in input_dict:
            raise KeyError(f"Could not find key numberOfChildren in input data: {input_dict}")
        if "familyComposition" not in input_dict:
            raise KeyError(f"Could not find key familyComposition in input data: {input_dict}")
        if "familyUnitInPayForDecember" not in input_dict:
            raise KeyError(f"Could not find key familyUnitInPayForDecember in input data: {input_dict}")

        # make sure that every value is having the correct type
        if type(input_dict["id"]) is not str:
            raise TypeError(f"id type expect to be str, got {type(input_dict["id"])}")
        if type(input_dict["numberOfChildren"]) is not int:
            raise TypeError(f"numberOfChildren type expect to be int, got {type(input_dict["numberOfChildren"])}")
        if type(input_dict["familyComposition"]) is not str:
            raise TypeError(f"familyComposition type expect to be str, got {type(input_dict["numberOfChildren"])}")
        if type(input_dict["familyUnitInPayForDecember"]) is not bool:
            raise TypeError(f"familyUnitInPayForDecember type expect to be bool, got {type(input_dict["numberOfChildren"])}")

        id: str = input_dict["id"]
        number_of_children: int = input_dict["numberOfChildren"]
        if number_of_children < 0:
            raise ValueError(f"numberOfChildren should not be negative, got {number_of_children}")
        if input_dict["familyComposition"] == FamilyCompositionType.SINGLE.value:
            family_composition: FamilyCompositionType = FamilyCompositionType.SINGLE
        elif input_dict["familyComposition"] == FamilyCompositionType.COUPLE.value:
            family_composition: FamilyCompositionType = FamilyCompositionType.COUPLE
        else:
            raise ValueError(f"familyComposition should be \"single\" or \"couple\", got {input_dict["familyComposition"]} instead")
        family_unit_in_pay_for_december: bool = input_dict["familyUnitInPayForDecember"]

        return WinterSupplementInput(id=id, number_of_children=number_of_children,
                                     family_composition=family_composition,
                                     family_unit_in_pay_for_december=family_unit_in_pay_for_december)


@dataclass
class WinterSupplementOutput:
    id: str
    is_eligible: bool
    base_amount: float = 0.0
    children_amount: float = 0.0
    supplement_amount: float = 0.0

    def get_dict(self) -> Dict:
        return {
            "id": self.id,
            "isEligible": self.is_eligible,
            "baseAmount": self.base_amount,
            "childrenAmount": self.children_amount,
            "supplementAmount": self.supplement_amount,
        }

    def get_json_str(self) -> str:
        """
        Return this output in json string format.
        Noted that the floats always have two decimal places, because this is for money, the smallest unit is cents.
        """
        json_dict = {
            "id": self.id,
            "isEligible": self.is_eligible,
            "baseAmount": f"{self.base_amount:.2f}",
            "childrenAmount": f"{self.children_amount:.2f}",
            "supplementAmount": f"{self.supplement_amount:.2f}",
        }
        # Because json.dumps couldn't set the float decimal easily
        # The floats related to money are converted into strings, and then use regex to trim the quotation marks
        json_str = json.dumps(json_dict)
        return WinterSupplementOutput.trim_string_into_float_in_json_str(json_str)

    @staticmethod
    def trim_string_into_float_in_json_str(json_str: str) -> str:
        """
        Trim possible string into float inside the json string
        :param json_str: floats in string format
        :return: floats in number format
        Example input:
        '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": false, "baseAmount": "0.00", "childrenAmount": "0.00", "supplementAmount": "0.00"}'
        example output:
        '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": false, "baseAmount": 0.00, "childrenAmount": 0.00, "supplementAmount": 0.00}'
        """
        str_output = re.sub(r"(\")(\d+\.\d{2})(\")", r"\2", json_str)
        return str_output
