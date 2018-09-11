from test_framework import generic_test



def palindrome_decompositions(input):
    res = []

    def gen_palin(prefix=[], word=""):
        if not word:
            res.append(list(prefix))
        for i, a in enumerate(word):
            if a == word[0]:
                if word[:i+1] == word[:i+1][::-1]:
                    gen_palin(prefix + [word[0:i+1]], word[i+1:])

    gen_palin([], input)

    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
