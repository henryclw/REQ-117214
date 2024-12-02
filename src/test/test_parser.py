import unittest

from structure.winter_supplement import FamilyCompositionType
from utils.json_parser import read_winter_supplement_input


class TestParser(unittest.TestCase):

    def test_bad_010(self):
        with open("./test/test_parser_examples/bad_010_input.json") as f:
            json_str = f.read()
            with self.assertRaises(KeyError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_bad_020(self):
        with open("./test/test_parser_examples/bad_020_input.json") as f:
            json_str = f.read()
            with self.assertRaises(TypeError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_bad_030(self):
        with open("./test/test_parser_examples/bad_030_input.json") as f:
            json_str = f.read()
            with self.assertRaises(ValueError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_bad_031(self):
        with open("./test/test_parser_examples/bad_031_input.json") as f:
            json_str = f.read()
            with self.assertRaises(ValueError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_good_010(self):
        with open("./test/test_parser_examples/good_010_input.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 2)
            self.assertEqual(winter_supplement_input.family_composition, FamilyCompositionType.SINGLE)
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)


if __name__ == '__main__':
    unittest.main()
