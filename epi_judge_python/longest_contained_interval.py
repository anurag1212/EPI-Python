from test_framework import generic_test


def longest_contained_range(A):
    A, d = {a: i for i, a in enumerate(A)}, float('-inf')
    for v in A:
        if A[v] is not None:
            my_v, count = v, 0
            while v in A and A[v] is not None:
                count += 1
                A[v] = None
                v -= 1
            v = my_v + 1
            while v in A and A[v] is not None:
                count += 1
                A[v] = None
                v += 1
            d = max(d, count)

    return d


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
