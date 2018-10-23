from test_framework import generic_test


def majority_search(stream):
    i, c, cand = next(stream, None), 0, ""
    while i:
        if c:
            if i == cand:
                c += 1
            else:
                c -= 1
        else:
            cand, c = i, 1
        i = next(stream, None)
    return cand


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
