from test_framework import generic_test
import collections


def examine_buildings_with_sunset(sequence):
    res = []
    building = collections.namedtuple("building", ("i", "h"))
    for i, h in enumerate(sequence):
        curr = building(i, h)
        if not res:
            res.append(curr)
        else:
            while res and res[-1].h <= curr.h:
                res.pop()
            res.append(curr)
    return list(reversed([r.i for r in res]))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
