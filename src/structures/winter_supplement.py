from dataclasses import dataclass


@dataclass
class WinterSupplementInput:
    id: str
    number_of_children: int
    family_composition: str
    family_unit_in_pay_for_december: bool

    @staticmethod
    def new_one_from_dict(input_dict):
        assert "id" in input_dict and "numberOfChildren" in input_dict
        assert "familyUnitInPayForDecember" in input_dict, "Could not find key familyUnitInPayForDecember in input data"
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
