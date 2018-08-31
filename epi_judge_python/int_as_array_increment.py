from test_framework import generic_test


def plus_one(A):
    carry, i = 1, len(A) - 1
    while carry:
        if i == -1:
            A.insert(0, 1)  # Idiot, append 0 instead of inserting 1
            carry = 0
        else:
            A[i] += carry
            if not A[i] % 10:
                A[i] %= 10
                carry = 1
            else:
                carry = 0
        i -= 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
