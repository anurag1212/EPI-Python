from test_framework import generic_test


def ss_decode_col_id(col):
    res, power = 0, 0
    for char in reversed(col):
        res, power = res + (26 ** power) * (ord(char) - 64), power + 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
