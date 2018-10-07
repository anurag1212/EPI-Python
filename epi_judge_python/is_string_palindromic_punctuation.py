from test_framework import generic_test


def is_palindrome(s):
    begin, end = 0, len(s)-1
    while begin <= end:
        while not s[begin].isalnum() and begin <= end and begin < len(s) - 1:
            begin += 1
        while not s[end].isalnum() and end >= begin and end > 0:
            end -= 1
        if s[begin].lower() != s[end].lower():
            return False
        begin += 1
        end -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
