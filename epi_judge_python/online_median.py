from test_framework import generic_test
import heapq


def balance_heaps(minh, maxh):
    mn = len(minh)
    mx = len(maxh)
    if mn > mx:
        heapq.heappush(maxh, -heapq.heappop(minh))

    if mx > mn + 1:
        heapq.heappush(minh, -heapq.heappop(maxh))


def get_median(minh, maxh):
    if not minh:
        return -maxh[0]
    if not maxh:
        return minh[0]
    if len(maxh) == len(minh):
        return (-maxh[0] + minh[0])/2
    else:
        return -maxh[0]


def online_median(sequence):
    e = next(sequence, None)
    maxheap, minheap, medians = [], [], []
    while e is not None:
        if minheap and maxheap:
            if e < minheap[0]:
                heapq.heappush(maxheap, -e)
            else:
                heapq.heappush(minheap, e)

        else:
            if not maxheap:
                heapq.heappush(maxheap, -e)
            elif not minheap:
                if -maxheap[0] > e:
                    heapq.heappush(minheap, -heapq.heappop(maxheap))
                    heapq.heappush(maxheap, -e)
                else:
                    heapq.heappush(minheap, e)

        balance_heaps(minheap, maxheap)
        medians.append(get_median(minheap, maxheap))
        e = next(sequence, None)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
