from test_framework import generic_test


def is_balanced_binary_tree(tree):

    def h(root):
        if root is None: return -1

        l = h(root.left)
        if l is False: return False

        r = h(root.right)
        if r is False: return False

        if abs(l-r) > 1: return False
        return 1 + max(l, r)

    return True if h(tree) is not False else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
