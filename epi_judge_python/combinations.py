from test_framework import generic_test, test_utils


def combinations_book(n, k):
    # Average running time:  343 us
    # Median running time:    35 us
    def d_c(o, p_c):
        if len(p_c) == k:
            res.append(list(p_c))
            return
        n_r = k - len(p_c)
        i = o
        while i<=n and n_r <= n-i+1:
            d_c(i+1, p_c + [i])
            i+=1
    res = []
    d_c(1, [])
    return res


def combinations_1(n, k):
    # Average running time:    1 ms
    # Median running time:   160 us
    result = []

    def pset(res, A):
        if len(res) == k:
            result.append(list(res))
        else:
            seen = set()
            for a in A:
                if a not in seen:
                    seen.add(a)
                    pset(res | {a}, A - seen)

    pset(set(), set(range(1, n+1)))
    return result


def combinations(n, k):
    # Average running time:    1 ms
    # Median running time:   173 us
    result = []

    def pset(res, A, last_added):
        if len(res) == k:
            result.append(list(res))
            res -= last_added
        else:
            seen = set()
            for a in A:
                if a not in seen:
                    seen.add(a)
                    pset(res | {a}, A - seen, {a})

    pset(set(), set(range(1, n+1)), set())
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
