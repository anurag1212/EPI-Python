from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s):
    n = 0
    for item in Counter(s).items():
        if item[1] % 2: n += 1
    return n <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
