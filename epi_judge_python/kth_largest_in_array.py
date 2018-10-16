from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    while True:
        pivot, smaller, larger = A[0], [], []
        for i in range(1, len(A)):
            if A[i] < pivot:
                smaller.append(A[i])
            elif A[i] >= pivot:
                larger.append(A[i])
        if len(larger) == k-1:
            return pivot
        elif len(larger) > k-1:
            A = larger
        elif len(larger) < k-1:
            A, k = smaller, k - len(larger) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
