from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    res = []

    def k_largest(root):
        if not root: return
        k_largest(root.right)
        if len(res) == k: return
        res.append(root.data)
        k_largest(root.left)

    k_largest(tree)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
