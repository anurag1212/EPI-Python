from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    heap, res = [(a[0], i, 0) for i, a in enumerate(sorted_arrays)], []
    heapq.heapify(heap)
    while heap:
        e, arr_idx, ele_idx = heapq.heappop(heap)
        res.append(e)
        if ele_idx + 1 < len(sorted_arrays[arr_idx]):
            heapq.heappush(heap, (sorted_arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
