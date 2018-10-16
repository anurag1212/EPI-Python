from test_framework import generic_test


def search_smallest(A):
    lo, hi, mid = 0, len(A) - 1, -2
    while lo <= hi:
        if A[lo] < A[hi]:
            return lo
        mid = (lo + hi) // 2
        if A[lo] > A[mid]:
            hi = mid
        elif A[lo] < A[mid]:
            lo = mid
        elif A[lo] == A[mid]:
            return mid + 1 if mid + 1 < len(A) else mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
