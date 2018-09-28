from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence):

    if not preorder_sequence: return

    class Tree:
        __slots__ = "left", "right", "data"

        def __init__(self, d):
            self.left = None
            self.right = None
            self.data = d

    def rebuild(lo=float('-inf'), hi=float('inf')):
        root = preorder_sequence[ptr[0]]
        if not lo <= root <= hi: return None
        root = Tree(root)
        if ptr[0] + 1 < len(preorder_sequence):
            ptr[0] += 1
            root.left = rebuild(lo, root.data)
            root.right = rebuild(root.data, hi)
        return root

    ptr = [0]
    return rebuild()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
