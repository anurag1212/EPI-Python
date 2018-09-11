from test_framework import generic_test, test_utils


def permutations(A):
    results = []

    def permute(unused, res):
        if len(res) == len(A):
            results.append(list(res))
            return
        for e in A:
            if unused[e]:
                res.append(e)
                unused[e] = False
                permute(unused, res)
                unused[e] = True
                res.pop()

    for a in A:
        unused_dict = {i: True for i in A}
        unused_dict[a] = False
        permute(unused_dict, [a])
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
