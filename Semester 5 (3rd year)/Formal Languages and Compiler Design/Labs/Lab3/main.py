from analyzer import Analyzer


# Test that the analyzer works
scan = Analyzer('program1.txt', 'token.in')
scan.analyzeFile()

# scan = Analyzer('program2.txt', 'token.in')
# scan.analyzeFile()

# scan = Analyzer('program3.txt', 'token.in')
# scan.analyzeFile()
#
# scan = Analyzer('program_error.txt', 'token.in')
# scan.analyzeFile()