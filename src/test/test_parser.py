import unittest

from utils.json_parser import read_winter_supplement_input


class TestParser(unittest.TestCase):

    def test_bad_1(self):
        with open("./test/test_parser_examples/bad_1_input.json") as f:
            json_str = f.read()
            with self.assertRaises(AssertionError):
                winter_supplement_input = read_winter_supplement_input(json_str)

    def test_good_1(self):
        with open("./test/test_parser_examples/good_1_input.json") as f:
            json_str = f.read()
            winter_supplement_input = read_winter_supplement_input(json_str)
            self.assertEqual(winter_supplement_input.id, "f48912a6-41b6-48dd-a610-a922984a0e37")
            self.assertEqual(winter_supplement_input.number_of_children, 12)
            self.assertEqual(winter_supplement_input.family_composition, "single")
            self.assertEqual(winter_supplement_input.family_unit_in_pay_for_december, True)


if __name__ == '__main__':
    unittest.main()
