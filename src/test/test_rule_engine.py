import unittest

from engine.rule_engine import calculate_eligible_supplement
from structure.winter_supplement import FamilyCompositionType, WinterSupplementInput


class TestParser(unittest.TestCase):

    def test_rule_engine_bad_010(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=-3,
            family_composition=FamilyCompositionType.SINGLE,
            family_unit_in_pay_for_december=True
        )
        with self.assertRaises(ValueError):
            winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)

    def test_rule_engine_good_010(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=0,
            family_composition=FamilyCompositionType.SINGLE,
            family_unit_in_pay_for_december=True
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, True)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 60)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 60)

    def test_rule_engine_good_011(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=0,
            family_composition=FamilyCompositionType.COUPLE,
            family_unit_in_pay_for_december=True
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, True)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 120)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 120)

    def test_rule_engine_good_012(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=2,
            family_composition=FamilyCompositionType.SINGLE,
            family_unit_in_pay_for_december=True
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, True)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 120)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 40)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 160)

    def test_rule_engine_good_013(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=3,
            family_composition=FamilyCompositionType.COUPLE,
            family_unit_in_pay_for_december=True
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, True)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 120)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 60)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 180)

    def test_rule_engine_good_020(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=0,
            family_composition=FamilyCompositionType.SINGLE,
            family_unit_in_pay_for_december=False
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, False)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 0)

    def test_rule_engine_good_021(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=0,
            family_composition=FamilyCompositionType.COUPLE,
            family_unit_in_pay_for_december=False
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, False)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 0)

    def test_rule_engine_good_022(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=2,
            family_composition=FamilyCompositionType.SINGLE,
            family_unit_in_pay_for_december=False
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, False)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 0)

    def test_rule_engine_good_023(self):
        winter_supplement_input = WinterSupplementInput(
            id="5243e4c8-c021-4fbc-b45d-59e5dc951adf",
            number_of_children=3,
            family_composition=FamilyCompositionType.COUPLE,
            family_unit_in_pay_for_december=False
        )
        winter_supplement_output = calculate_eligible_supplement(winter_supplement_input)
        self.assertEqual(winter_supplement_output.id, winter_supplement_input.id)
        self.assertEqual(winter_supplement_output.is_eligible, False)
        self.assertAlmostEqual(winter_supplement_output.base_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.children_amount, 0)
        self.assertAlmostEqual(winter_supplement_output.supplement_amount, 0)


if __name__ == '__main__':
    unittest.main()
