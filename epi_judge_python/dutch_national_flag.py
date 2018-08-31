import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    start, end, p = 0, len(A) - 1, A[pivot_index]

    def move_boundaries(s, e):
        while A[s] < p:
            s += 1
        while A[e] > p:
            e -= 1
        return s, e

    start, end = move_boundaries(start, end)
    i = start
    while i <= end:
        swap = False
        if A[i] < p and i > start:  # Mistake 2, did not put the check if i > start
            # print("Swapped i", i, A[i], " and start ", start, A[start])
            A[i], A[start] = A[start], A[i]
            swap = True
        elif A[i] > p and i < end:  # Mistake 2, did not put the check if i < end
            # print("Swapped i", i, A[i], " and end ", end, A[end])
            A[i], A[end] = A[end], A[i]
            swap = True
        if swap and A[i] != p:
            i -= 1
        i += 1  # Mistake 1, had put this line before the check, causing the check to be incorrect
        start, end = move_boundaries(start, end)
    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
