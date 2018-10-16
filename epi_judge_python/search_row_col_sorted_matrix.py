from test_framework import generic_test


def matrix_search(A, x):
    curr = [0, len(A[0])-1]
    while curr[0] < len(A) and curr[1] > -1:
        if A[curr[0]][curr[1]] == x:
            return True
        elif A[curr[0]][curr[1]] < x:
            curr[0] += 1
        else:
            curr[1] -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
