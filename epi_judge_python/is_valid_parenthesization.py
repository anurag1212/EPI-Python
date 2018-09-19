from test_framework import generic_test


def is_well_formed(s):
    opens = ['(', '{', '[']
    close = [')', '}', ']']
    ptr = 0
    stk = []
    while ptr < len(s):
        if s[ptr] in opens:
            stk.append(s[ptr])
        else:
            if stk and close.index(s[ptr]) == opens.index(stk[-1]):
                stk.pop()
            else:
                return False
        ptr += 1
    return True if not stk else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
