from test_framework import generic_test


def reverse_bits(x):
    size = 0
    y = x
    ans = 0
    count = 0
    while y:
        y >>= 1
        size += 1
    while size:
        count += 1
        size -= 1
        bit = (x >> size) & 1
        if bit:
            ans ^= 2**count
    ans <<= 63-count
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))