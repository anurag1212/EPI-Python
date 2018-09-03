from test_framework import generic_test


def generate_pascal_triangle(n):
    pascal = [[1] * (i+1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    return pascal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
