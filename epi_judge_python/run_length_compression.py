from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    res, i = [], 0
    while i < len(s):
        num = []
        while i < len(s) and s[i].isdigit():
            num.append(s[i])
            i += 1
        num = int("".join(num))
        res.extend([s[i]] * num)
        i += 1
    return "".join(res)


def encoding(s):
    ret, count = [], 1
    for i in range(len(s)):
        if i+1 == len(s) or s[i+1] != s[i]:
            ret.extend([str(count), s[i]])
            count = 1
        else:
            count += 1
    return "".join(ret)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
