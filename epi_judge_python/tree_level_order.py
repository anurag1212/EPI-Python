from test_framework import generic_test
import collections


def binary_tree_depth_order(tree):
    if not tree: return []
    q = collections.deque()
    q.append(tree)
    q.append(None)
    res = []
    curr_level = []
    while q:
        curr = q.popleft()
        if curr is None:
            if q:
                q.append(None)
            res.append(list(curr_level))
            curr_level = []
        else:
            curr_level.append(curr.data)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
