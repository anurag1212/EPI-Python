from test_framework import generic_test


def rotate_matrix(square_matrix):

    def rotate_layer(s, n):

        def replace(c1):
            square_matrix[c1[0]][c1[1]], start["value"] = start["value"], square_matrix[c1[0]][c1[1]]
            return

        if n <= 1:
            return

        last = s+n-1
        start = None

        for i in range(s, s+n-1):
            start = {"value": square_matrix[s][i]}
            print(start)
            replace(((i-s), last))
            replace((last, last-(i-s)))
            replace((last-(i-s), s))
            replace((s, s+(i-s)))

    size, num = len(square_matrix), len(square_matrix)
    for layer in range(0, (size-1)//2+1):
        rotate_layer(layer, num)
        layer, num = layer + 1, num - 2

    return square_matrix


st=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for a in rotate_matrix(st):
    print(a)


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("matrix_rotation.py",
#                                        'matrix_rotation.tsv',
#                                        rotate_matrix_wrapper))
