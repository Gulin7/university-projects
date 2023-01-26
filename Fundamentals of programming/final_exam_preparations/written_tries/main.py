import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['A', 'B', 'C']
table.hrules = prettytable.ALL
table.header = True
table.add_row([1, 2, 3])
table.add_row([1, 2, 3])
table.add_row([1, 2, 3])
table.add_column('B', [4, 4, 4])
print(table)

sentence = 'Mama, nacho, taco'
sentence = sentence.split(', ')
print(sentence)