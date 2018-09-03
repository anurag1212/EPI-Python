from test_framework import generic_test


def next_permutation(perm):
    prev = float("-inf")
    for i in range(len(perm)-1,-1,-1):
        if perm[i] < prev:
            for j in range(len(perm)-1,-1,-1):
                if perm[j] > perm[i]:
                    perm[i], perm[j] = perm[j], perm[i]
                    if i+1 <= len(perm)-1:
                        a = perm[i+1:]
                        a.reverse()  # Lazy, should do it in place
                        perm = perm[:i+1]+a
                    return perm
        else:
            prev = perm[i]
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
