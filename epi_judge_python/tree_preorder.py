from test_framework import generic_test
import queue


def preorder_traversal(tree):
    stk, traversal, visited = [], [], set()
    while stk or tree:
        if tree:
            stk.append(tree)
            traversal.append(tree.data)
            tree = tree.left
        else:
            tree = stk.pop()
            tree = tree.right

    return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
