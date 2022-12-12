from root.services.conversions import *
from root.services.rapid_conversions import *
from root.services.functions import *


def run_rapid_conversions_tests():
    num_base_2 = 110101
    num_base_4 = 123102
    num_base_8 = 75421
    num_base_16 = '1b'
    assert int(rapid_convert_to_base2_from_given_base(num_base_16, 16)) == 11011
    assert int(rapid_convert_to_base2_from_given_base(num_base_4, 4)) == 11011010010
    assert int(rapid_convert_to_base2_from_given_base(num_base_8, 8)) == 111101100010001
    assert int(rapid_convert_from_base2_to_given_base(num_base_2, 4)) == 311
    assert int(rapid_convert_from_base2_to_given_base(num_base_2, 8)) == 65
    assert int(rapid_convert_from_base2_to_given_base(num_base_2, 16)) == 35


def run_conversions_tests():
    num_base_7 = 12345
    num_base_10 = 1298
    num_base_10_2 = 1241
    num_base_10_3 = 1659
    num_base_3 = 2210
    num_base_8 = 74261235
    assert (int(convert_from_base10_to_base(num_base_10, 6)) == 10002)
    assert (int(convert_to_base10(num_base_7, 7)) == 3267)
    assert (int(convert_from_base10_to_base(num_base_10_2, 9)) == 1628)
    assert (int(convert_to_base10(num_base_3, 3)) == 75)
    assert (int(convert_from_base10_to_base(num_base_10_3, 5)) == 23114)
    assert (int(convert_to_base10(num_base_8, 8)) == 15819421)


def run_all_tests():
    run_rapid_conversions_tests()
    run_conversions_tests()
    print("✔ Tests passed! 👏🎉😎")
