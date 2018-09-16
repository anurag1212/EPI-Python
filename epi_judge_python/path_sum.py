from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    remaining_weight -= tree.data
    if not tree.left and not tree.right:
        return False if remaining_weight else True
    if tree.left:
        l = has_path_sum(tree.left, remaining_weight)
        if l: return l
    if tree.right:
        r = has_path_sum(tree.right, remaining_weight)
        if r: return r
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
