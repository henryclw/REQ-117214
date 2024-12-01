from dataclasses import dataclass


@dataclass
class WinterSupplementInput:
    id: str
    number_of_children: int
    family_composition: str
    family_unit_in_pay_for_december: bool

    @staticmethod
    def new_one_from_dict(input_dict):

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

        # make sure
        if input_dict["familyComposition"] not in ["single", "couple"]:
            raise ValueError(f"familyComposition should be \"single\" or \"couple\", got {input_dict["familyComposition"]} instead")

        id: str = input_dict["id"]
        number_of_children: int = input_dict["numberOfChildren"]
        family_composition: str = input_dict["familyComposition"]
        family_unit_in_pay_for_december: bool = input_dict["familyUnitInPayForDecember"]
        return WinterSupplementInput(id=id, number_of_children=number_of_children,
                                     family_composition=family_composition,
                                     family_unit_in_pay_for_december=family_unit_in_pay_for_december)


@dataclass
class WinterSupplementOutput:
    id: str
    isEligible: bool
    baseAmount: float
    childrenAmount: float
    supplementAmount: float

    def get_dict(self):
        # TODO: float point limit to .2f
        return {
            "id": self.id,
            "isEligible": self.isEligible,
            "baseAmount": self.baseAmount,
            "childrenAmount": self.childrenAmount,
            "supplementAmount": self.supplementAmount,
        }
