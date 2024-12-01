from src.utils.json_parser import read_winter_supplement_input

if __name__ == "__main__":
    with open("test/test_parser_examples/bad_010_input.json") as f:
        json_str = f.read()
        print(read_winter_supplement_input(json_str))

