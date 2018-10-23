from test_framework import generic_test


def has_two_sum(A, t):
    start, end = 0, len(A) - 1
    while start <= end:
        candidate_sum = A[start] + A[end]
        if candidate_sum == t:
            return True
        elif candidate_sum > t:
            end -= 1
        else:
            start += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
