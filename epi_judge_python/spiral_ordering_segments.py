from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    def add_layer(s, n):
        if n == 1:
            spiral_ordering.append(square_matrix[s][s])
            return
        last = s+n-1
        for i in range(s, last):
            spiral_ordering.append(square_matrix[s][i])
        for i in range(s, last):
            spiral_ordering.append(square_matrix[i][last])
        for i in range(last, s, -1):
            spiral_ordering.append(square_matrix[last][i])
        for i in range(last, s, -1):
            spiral_ordering.append(square_matrix[i][s])
        return

    spiral_ordering, num, layer = [], len(square_matrix), 0
    while num > 0:
        add_layer(layer, num)
        layer, num = layer + 1, num - 2
    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
