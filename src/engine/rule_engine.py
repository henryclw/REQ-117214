import logging

from structure.winter_supplement import WinterSupplementInput, WinterSupplementOutput, FamilyCompositionType


logger = logging.getLogger(__name__)


def calculate_eligible_supplement(winter_supplement_input: WinterSupplementInput) -> WinterSupplementOutput:
    logger.debug(f"Got winter_supplement_input: {winter_supplement_input}")
    is_eligible = winter_supplement_input.family_unit_in_pay_for_december
    output: WinterSupplementOutput = WinterSupplementOutput(
        id=winter_supplement_input.id,
        is_eligible=is_eligible
    )
    if not is_eligible:  # return 0 for the non-eligible family
        logger.debug(f"Return non-eligible output: {output}")
        return output
    else:  # eligible
        if winter_supplement_input.number_of_children == 0:  # childless family
            if winter_supplement_input.family_composition is FamilyCompositionType.SINGLE:
                output.base_amount = 60
            elif winter_supplement_input.family_composition is FamilyCompositionType.COUPLE:
                output.base_amount = 120
            else:
                raise ValueError(f"Unknown FamilyCompositionType, got {winter_supplement_input.family_composition}")
        elif winter_supplement_input.number_of_children > 0:  # family with children
            output.base_amount = 120
            output.children_amount = winter_supplement_input.number_of_children * 20
        else:
            raise ValueError(f"Number of children should not be negative, got {winter_supplement_input.number_of_children}")

        # the supplement amount is the sum
        output.supplement_amount = output.base_amount + output.children_amount
        logger.debug(f"Return eligible output: {output}")
        return output
