from test_framework import generic_test


value_of = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def convert_base(num_as_string, b1, b2):

    neg = [False]
    if num_as_string[0] == "-": neg, num_as_string = [True], num_as_string[1:]

    def to_10(s, b):
        power, res = 0, 0
        for digit in reversed(s):
            res, power = res + value_of.index(digit) * b ** power, power + 1
        return res

    def from_10(n, b):
        res = []
        if not n: res.append("0")
        while n:
            rem, n = n % b, n // b
            res.append(value_of[rem])
        if neg[0]: res.append('-')
        return ''.join(reversed(res))

    return from_10(to_10(num_as_string, b1), b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
