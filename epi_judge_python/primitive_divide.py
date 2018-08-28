from test_framework import generic_test


def divide(x, y):
    if not x or not y or x < y:
        return 0

    k, diff = get_max_pow(x, y)
    q = 2**k
    big_y = y << k
    while diff > y:
        while big_y > diff:
            big_y >>= 1
            k -= 1
        q += 2**k
        diff = diff - big_y

    return q+1 if diff == y else q


def get_max_pow(x, y):
    count = 0
    if y == x:
        return 0, 0
    while y < x:
        y <<= 1
        count += 1
    y >>= 1
    return count-1, x-y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
