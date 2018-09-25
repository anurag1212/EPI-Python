from test_framework import generic_test
import heapq


def sort_k_increasing_decreasing_array(A):
    start, ptr, inc = 0, 0, False
    incs, decs, res = [], [], []
    if A[0] <= A[1]: inc = True
    while ptr < len(A):
        if inc:
            if ptr + 1 == len(A) or A[ptr + 1] < A[ptr]:
                if ptr + 1 == len(A): ptr += 1
                incs.append((start, ptr))
                start = ptr
                inc = not inc
        else:
            if ptr + 1 == len(A) or A[ptr + 1] > A[ptr]:
                if ptr + 1 == len(A): ptr += 1
                decs.append((start, ptr))
                start = ptr
                inc = not inc
        ptr += 1

    heap = [(A[tup[0]], 1, tup[0], tup[1]-tup[0]) for tup in incs]
    heap.extend([(A[tup[1]-1], -1, tup[1]-1, tup[1]-tup[0]) for tup in decs])
    heapq.heapify(heap)

    while heap:
        e, increment, arr_idx, num_left = heapq.heappop(heap)
        res.append(e)
        if num_left - 1:
            heapq.heappush(heap, (A[arr_idx + increment], increment, arr_idx + increment, num_left - 1))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
