from test_framework import generic_test


def power(x, y):
    diff, ans, sign = y, 1, True
    if not x:
        return 0
    if not y:
        return 1
    if y < 0:
        sign = False
    while diff:
        if sign:
            exp, big_x = 1, x
            while exp * 2 <= diff:
                big_x *= big_x
                exp *= 2
        else:
            exp, big_x = -1, 1/x
            while exp * 2 >= diff:
                big_x *= big_x
                exp *= 2
        ans *= big_x
        diff -= exp
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
