from test_framework import generic_test


def square_root(x):
    lo, hi= 0, max(1,x)
    while lo < hi:
        mid = (lo + hi) / 2
        if lo == mid or hi == mid: return mid  # Should've got this without prints
        if mid ** 2 < x:
            lo = mid
        elif mid ** 2 > x:
            hi = mid
        else:
            return mid
    return mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
