from test_framework import generic_test


def closest_int_same_bit_count(x):
    if x & 1:
        y = x
        count = 0
        while y & 1 == 1:
            y >>= 1
            count += 1
    else:
        y = x
        count = 0
        while y & 1 == 0:
            y >>= 1
            count += 1
    x ^= (1 << count | 1 << (count-1))
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
