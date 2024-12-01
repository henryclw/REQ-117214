from dataclasses import dataclass


@dataclass
class WinterSupplementInput:
    #  = dataclasses.field(metadata={"alias":"@name"})
    id: str
    numberOfChildren: int
    familyComposition: str
    familyUnitInPayForDecember: bool

    @staticmethod
    def new_one_from_dict(input_dict):
        assert "id" in input_dict and "numberOfChildren" in input_dict
        id: str = input_dict["id"]
        numberOfChildren: int = input_dict["numberOfChildren"]
        familyComposition: str = input_dict["familyComposition"]
        familyUnitInPayForDecember: bool = input_dict["familyUnitInPayForDecember"]
        return WinterSupplementInput(id=id, numberOfChildren=numberOfChildren, familyComposition=familyComposition, familyUnitInPayForDecember=familyUnitInPayForDecember)


@dataclass
class WinterSupplementOutput:
    id: str
    isEligible: bool
    baseAmount: float
    childrenAmount: float
    supplementAmount: float
