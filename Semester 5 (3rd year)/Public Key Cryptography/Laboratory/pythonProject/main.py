from testSymbolTableWithConstants import TestSymbolTableWithConstants
from testSymbolTableWithIdentifiers import TestSymbolTableWithIdentifiers

def runTests():
    print('Run tests with identifiers')
    testIdentifier = TestSymbolTableWithIdentifiers()
    testIdentifier.runTests()

    print('Run tests with constants')
    testConstants = TestSymbolTableWithConstants()
    testConstants.runTests()

    print('All tests passed')

if __name__ == '__main__':
    runTests()
