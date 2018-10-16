from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream):
    i = next(stream, None)
    xor, total, count = 0, 0, 0
    while i is not None:
        total += i
        xor ^= i
        count += 1
        i = next(stream, None)
    mod = count % 4
    if mod == 0:
        expected_xor = count
    elif mod == 1:
        expected_xor = 1
    elif mod == 2:
        expected_xor = 3
    else:
        expected_xor = 0

    print(total, count)
    diff = total - (count*(count-1))//2
    print(diff)
    missing_is_greater = True
    if diff > 0:
        missing_is_greater = False
    diff = abs(diff)

    for i in range(diff, count):
        j = i - diff
        if xor ^ (i ^ j) == expected_xor:
            return i if missing_is_greater else j

    return -1


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
