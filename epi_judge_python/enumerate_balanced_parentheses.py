from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs, res=[]):
    def generate_parens(left_needed, right_needed, string=""):
        if left_needed > 0:
            generate_parens(left_needed-1, right_needed, string+"(")
        if left_needed < right_needed:
            generate_parens(left_needed, right_needed-1, string+")")
        if not right_needed:
            res.append(string)
    generate_parens(num_pairs, num_pairs)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
