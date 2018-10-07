from test_framework import generic_test


def rabin_karp(t, s):
    if len(s) > len(t): return -1
    s_hash, t_hash = 0, 0
    for i, a in enumerate(s):
        s_hash += ord(a) * 26 ** (len(s) - i - 1)
    for i, a in enumerate(t[:len(s)]):
        t_hash += ord(a) * 26 ** (len(s) - i - 1)
    for i in range(len(s), len(t)):
        if s_hash == t_hash:
            if s == t[i-len(s):i]: return i-len(s)
        t_hash -= ord(t[i-len(s)]) * (26 ** (len(s) - 1))
        t_hash *= 26
        t_hash += ord(t[i])

    if s_hash == t_hash:
        if s == t[-len(s):]: return len(t) - len(s)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
