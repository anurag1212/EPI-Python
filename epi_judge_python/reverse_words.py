import functools


from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):

    def reverse_word(strt, end):
        while strt < end:
            s[strt], s[end] = s[end], s[strt]
            strt += 1
            end -= 1

    ptr = 0
    while ptr < len(s):
        start = ptr
        while ptr < len(s) and s[ptr] != ord(' '):
            ptr += 1
        reverse_word(start, ptr-1)
        ptr += 1

    s.reverse()
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
