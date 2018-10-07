from test_framework import generic_test
from test_framework.test_failure import TestFailure


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def int_to_string(x):
    result, neg = [], False
    if not x: return nums[0]
    if x < 0:
        neg, x = True, x*1
    while x:
        digit, x = x % 10, x//10
        result.append(nums[digit])
    if neg:
        result.append("-")
    result.reverse()
    return ''.join(result)


def string_to_int(s):
    result, power = 0, 0
    for i in range(len(s)):
        if s[~i] in nums:
            result, power = result + nums.index(s[~i]) * 10**power, power + 1
        else:
            result = -result
    return result


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
