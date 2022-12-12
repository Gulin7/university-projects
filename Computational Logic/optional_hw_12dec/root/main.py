from root.console.console import run_console
from root.tests.tests import run_all_tests


def main():
    run_all_tests()
    run_console()


if __name__ == '__main__':
    main()
