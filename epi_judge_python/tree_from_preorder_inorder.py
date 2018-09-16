from test_framework import generic_test


class BinaryTreeNode():
    __slots__ = "data", "left", "right"

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def binary_tree_from_preorder_inorder(preorder, inorder):
    if not preorder: return None

    root = preorder[0]
    inorder_root_idx = inorder.index(root)

    inorder_left = inorder[0:inorder_root_idx]
    inorder_right = inorder[inorder_root_idx+1:]

    preorder_left = preorder[1:inorder_root_idx+1]
    preorder_right = preorder[inorder_root_idx+1:]

    left_subtree = binary_tree_from_preorder_inorder(preorder_left, inorder_left)
    right_subtree = binary_tree_from_preorder_inorder(preorder_right, inorder_right)

    return BinaryTreeNode(root, left_subtree, right_subtree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
