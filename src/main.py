from src.utils.json_parser import read_winter_supplement_input

if __name__ == "__main__":
    with open("./test/test_rules/examples/ex_1_input.json") as f:
        ex_1_json_str = f.read()
        print(read_winter_supplement_input(ex_1_json_str))

