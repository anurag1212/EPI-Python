from test_framework import generic_test


def n_queens_1(n):

    results = []

    def place_queen(result, place_row):

        def is_safe(i, j):
            for row, col in enumerate([a for a in result if a is not None]):
                if i == row or j == col or (abs(i-row) == abs(j-col)):
                    return False
            return True

        if place_row == n:
            results.append(list(result))
            return

        for place_col in range(n):
            if is_safe(place_row, place_col):
                result[place_row] = place_col
                place_queen(result, place_row + 1)
                result[place_row] = None

    for first_col in range(n):
        placements = [None for _ in range(n)]
        placements[0] = first_col
        place_queen(placements, 1)

    return results


def n_queens(n):

    results = []

    def place_queen(result, place_row):

        def is_safe(i, j):
            for row, col in enumerate(result):
                if i == row or j == col or (abs(i-row) == abs(j-col)):
                    return False
            return True

        if place_row == n:
            results.append(list(result))
            return

        for place_col in range(n):
            if is_safe(place_row, place_col):
                result.append(place_col)
                place_queen(result, place_row + 1)
                result.pop()

    for first_col in range(n):
        place_queen([first_col], 1)

    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
