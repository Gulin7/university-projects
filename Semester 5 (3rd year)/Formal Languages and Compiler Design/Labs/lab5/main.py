from ll1 import Ll1

# Example usage
input_file = "g1.txt"  # Path to your grammar file
pif_file = "PIF.out"  # Path to your PIF output file

# Initialize Ll1 parser with grammar and PIF file
ll1 = Ll1(input_file=input_file, pif_file=pif_file)

# Print the generated parsing table
parsing_table = ll1.get_parsing_table()
for non_terminal, row in parsing_table.items():
    print(f"{non_terminal}: {dict(row)}")

# Input string to be parsed
input_string = "bcbc"

# Parse the input string using the LL1 parsing table
result = ll1.parse(input_string)

# Output whether the string is accepted or not by the grammar
if result:
    print(f"Input string '{input_string}' is accepted by the grammar.")
else:
    print(f"Input string '{input_string}' is NOT accepted by the grammar.")
