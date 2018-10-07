from test_framework import generic_test


def look_and_say(n):

    def gen_next(string):
        ret, count = [], 1
        for i in range(len(string)):
            if i+1 == len(string) or string[i+1] != string[i]:
                ret.extend([str(count), string[i]])
                count = 1
            else:
                count += 1
        return "".join(ret)

    prev = "1"
    while n-1:
        prev, n = gen_next(prev), n - 1

    return prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
