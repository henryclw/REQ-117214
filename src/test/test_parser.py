import unittest

from structure.winter_supplement import FamilyCompositionType, WinterSupplementOutput
from utils.json_parser import read_winter_supplement_input


class TestParser(unittest.TestCase):

    def test_input_bad_010(self):
        with open("./test/test_parser_examples/bad_input_010.json") as f:
            json_str = f.read()
            with self.assertRaises(KeyError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_input_bad_020(self):
        with open("./test/test_parser_examples/bad_input_020.json") as f:
            json_str = f.read()
            with self.assertRaises(TypeError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_input_bad_030(self):
        with open("./test/test_parser_examples/bad_input_030.json") as f:
            json_str = f.read()
            with self.assertRaises(ValueError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_input_bad_031(self):
        with open("./test/test_parser_examples/bad_input_031.json") as f:
            json_str = f.read()
            with self.assertRaises(ValueError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_input_good_010(self):
        with open("./test/test_parser_examples/good_input_010.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 0)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.SINGLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)

    def test_input_good_011(self):
        with open("./test/test_parser_examples/good_input_011.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 0)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.COUPLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)

    def test_input_good_012(self):
        with open("./test/test_parser_examples/good_input_012.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 2)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.SINGLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)

    def test_input_good_013(self):
        with open("./test/test_parser_examples/good_input_013.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 3)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.COUPLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)

    def test_input_good_020(self):
        with open("./test/test_parser_examples/good_input_020.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 0)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.SINGLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, False)

    def test_input_good_021(self):
        with open("./test/test_parser_examples/good_input_021.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 0)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.COUPLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, False)

    def test_input_good_022(self):
        with open("./test/test_parser_examples/good_input_022.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 2)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.SINGLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, False)

    def test_input_good_023(self):
        with open("./test/test_parser_examples/good_input_023.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 3)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.COUPLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, False)

    def test_output_good_010(self):
        winter_supplement_output = WinterSupplementOutput(
            id="9097bf53-50b6-47a3-92ca-f6adfa380c8b",
            is_eligible=False,
            base_amount=0.0,
            children_amount=0.0,
            supplement_amount=0.0
        )
        json_str_target = '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": false, "baseAmount": 0.00, "childrenAmount": 0.00, "supplementAmount": 0.00}'
        self.assertEqual(winter_supplement_output.get_json_str(), json_str_target)

    def test_output_good_020(self):
        winter_supplement_output = WinterSupplementOutput(
            id="9097bf53-50b6-47a3-92ca-f6adfa380c8b",
            is_eligible=True,
            base_amount=120,
            children_amount=40,
            supplement_amount=160
        )
        json_str_target = '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": true, "baseAmount": 120.00, "childrenAmount": 40.00, "supplementAmount": 160.00}'
        self.assertEqual(winter_supplement_output.get_json_str(), json_str_target)

    def test_output_good_021(self):
        winter_supplement_output = WinterSupplementOutput(
            id="9097bf53-50b6-47a3-92ca-f6adfa380c8b",
            is_eligible=True,
            base_amount=120.0,
            children_amount=40.0,
            supplement_amount=160.0
        )
        json_str_target = '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": true, "baseAmount": 120.00, "childrenAmount": 40.00, "supplementAmount": 160.00}'
        self.assertEqual(winter_supplement_output.get_json_str(), json_str_target)

    def test_output_good_022(self):
        winter_supplement_output = WinterSupplementOutput(
            id="9097bf53-50b6-47a3-92ca-f6adfa380c8b",
            is_eligible=True,
            base_amount=120.0,
            children_amount=40.00000000001,
            supplement_amount=159.99999999
        )
        json_str_target = '{"id": "9097bf53-50b6-47a3-92ca-f6adfa380c8b", "isEligible": true, "baseAmount": 120.00, "childrenAmount": 40.00, "supplementAmount": 160.00}'
        self.assertEqual(winter_supplement_output.get_json_str(), json_str_target)


if __name__ == '__main__':
    unittest.main()
