from test_framework import generic_test


def search_first_of_k(A, k):
    if not A: return -1
    lo, hi, res = 0, len(A) - 1, -1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if A[mid] < k:
            lo = mid + 1
        if A[mid] >= k:
            if A[mid] == k: res = mid
            hi = mid - 1
    return res

    # if A[lo] == k:
    #     return lo
    # if A[lo] < k and lo + 1 < len(A) and A[lo+1] == k:
    #     return lo+1
    # if A[lo] > k and lo > 0 and A[lo-1] == k:
    #     return lo-1
    # return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
