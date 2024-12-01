import argparse
import logging

from utils.json_parser import read_winter_supplement_input


logger = logging.getLogger(__name__)


if __name__ == "__main__":

    # the args for command line
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="This program is designed to solve the written assignment of the REQ117214",
        epilog=""
    )
    parser.add_argument("--log", help="the logging level of this program, the default level is INFO", default="INFO")
    args = parser.parse_args()

    # setting up logging configs, the logging level is from command line args
    numeric_level = getattr(logging, args.log, None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % args.log)
    logging.basicConfig(level=numeric_level,
                        format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")

    with open("./test/test_parser_examples/good_010_input.json") as f:
        json_str = f.read()
        winter_supplement_input = read_winter_supplement_input(json_str)
        print()
        logger.debug(f"Got winter_supplement_input: {winter_supplement_input}")
