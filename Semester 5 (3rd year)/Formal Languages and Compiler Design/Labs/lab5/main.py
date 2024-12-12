from ll1 import Ll1
from parser_output import ParserOutput


def main():
    input_file = "g1.txt"
    input_string = "abc"

    ll1 = Ll1(input_file=input_file)
    result = ll1.parse(input=input_string)

    if result:
        print(f"Input string {input_string} is accepted by the grammar {input_file}")

    else:
        print(f"Input string {input_string} is NOT accepted by the grammar {input_file}")

    parser_output = ParserOutput(ll1.get_parsed_table())
    parser_output.print_to_screen()
    parser_output.print_to_file('output.txt')


if __name__ == "__main__":
    main()