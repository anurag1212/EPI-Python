from test_framework import generic_test


def parity(x):
    # lookup = []
    # m = 2**16-1
    # for i in range(2**16):
    #     lookup.append(brute_parity(i))
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0b1

    # return lookup[x & m]


# def brute_parity(x):
#     result = 0
#     while x:
#         result ^= 1
#         x = x & x-1
#     return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
