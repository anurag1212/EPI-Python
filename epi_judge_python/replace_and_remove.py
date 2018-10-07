import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    num_a, res = 0, s
    last = None
    for i in range(len(res)):
        if res[i] == "a":
            num_a += 1
        if res[i] == "b":
            res[i] = None
            if last is None: last = i
        elif last is not None:
            res[last], res[i] = res[i], res[last]
            while res[last] is not None:
                last += 1

    shift = num_a
    res.extend([None] * shift)

    for i in range(last-1, -1, -1):
        if res[i] == 'a':
            res[i + shift], res[i + shift - 1] = 'd', 'd'
            shift -= 1
        else:
            res[i + shift] = res[i]

    if not res[-1]: res[-1] = ""
    return res


print(replace_and_remove(0, ['a', 'a', 'a', 'b', 'c', 'a', 'e', 'a', 'a']))


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
