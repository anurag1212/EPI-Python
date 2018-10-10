import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    begin, end, d, counter, keywords, res = 0, 0, float('inf'), collections.Counter(), collections.Counter(keywords), Subarray(0, 0)
    while end < len(paragraph):
        while end < len(paragraph) and (keywords - counter):
            if paragraph[end] in keywords:
                if paragraph[end] in counter:
                    counter[paragraph[end]] += 1
                else:
                    counter[paragraph[end]] = 1
            end += 1

        while not(keywords - counter) or counter == keywords:
            if end - begin + 1 < d:
                d = end - begin + 1
                res = Subarray(begin, end-1)
            if paragraph[begin] in counter:
                if counter[paragraph[begin]] == 1:
                    counter.pop(paragraph[begin])
                else:
                    counter[paragraph[begin]] -= 1
            begin += 1
    return res


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
