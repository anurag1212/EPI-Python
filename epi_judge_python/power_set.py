from test_framework import generic_test, test_utils


def generate_power_set(S):
    result = []

    def pset(res, A):
        seen = set()
        result.append(list(res))
        for a in A:
            if a not in seen:
                seen.add(a)
                pset(res | {a}, list(set(A)-seen))

    pset(set(), S)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
