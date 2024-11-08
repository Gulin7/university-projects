from analyzer import LexicalAnalyzer
from finiteautomata import FiniteAutomata

finiteAutomata = FiniteAutomata('FA.in')
finiteAutomata.start_menu()

# Test that the analyzer works
scan = LexicalAnalyzer('p1.txt', 'token.in')
scan.scan_file()

scan = LexicalAnalyzer('p2.txt', 'token.in')
scan.scan_file()

scan = LexicalAnalyzer('perr.txt', 'token.in')
scan.scan_file()