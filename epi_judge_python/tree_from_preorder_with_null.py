import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode():
    __slots__ = "data", "left", "right"

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def reconstruct_preorder(preorder):

    def reconstruct(preorder_iter):
        tree_key = next(preorder_iter)
        if tree_key is None: return None
        left_subtree = reconstruct(preorder_iter)
        right_subtree = reconstruct(preorder_iter)
        return BinaryTreeNode(tree_key, left_subtree, right_subtree)

    return reconstruct(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
