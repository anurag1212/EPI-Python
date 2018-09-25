from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    k += 1
    kheap = sequence[:k]
    heapq.heapify(kheap)
    for i in range(k, len(sequence)):
        sequence[i-k] = heapq.heappushpop(kheap, sequence[i])
    while kheap:
        sequence[-len(kheap)-1] = heapq.heappop(kheap)
    return sequence


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(sequence, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
