from src.tests.domain_tests import run_domain_tests
from src.tests.repository_tests import run_repository_tests
from src.tests.services_tests import run_service_tests


def run_all_tests():
    print('⌛Starting domain tests...')
    run_domain_tests()
    print('✅Finished domain tests!!! SIIIIUUUUUUUUU!!! 🆒')
    print('⌛Starting repository tests...')
    run_repository_tests()
    print('✅Finished repository tests!!! SIIIIUUUUUUUUU!!! 🆒')
    print('⌛Starting service tests...')
    run_service_tests()
    print('✅Finished service tests!!! SIIIIUUUUUUUUU!!! 🆒')
    print('🏆TESTS COMPLETED!🥇 TOTAL SUCCESS!!! 🤩')

