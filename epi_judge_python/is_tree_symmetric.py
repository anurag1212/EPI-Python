from test_framework import generic_test
import collections


def is_mirror(level):
    n = len(level)
    if n == 1:
        return True
    return level[:n//2] == list(reversed(level[n//2:]))


def is_symmetric_iter(tree):
    if not tree: return True
    root = tree
    q = collections.deque()
    q.append(root)
    q.append(None)
    one_level = []
    while q:
        curr = q.popleft()
        if curr is None:
            if q: q.append(None)
            if not is_mirror(one_level):
                return False
            one_level = []
        elif curr == 'e':
            one_level.append(curr)
        else:
            one_level.append(curr.data)
            for child in [curr.left, curr.right]:
                if child is None:
                    q.append('e')
                else:
                    q.append(child)

    return True


def is_symmetric(tree):

    def is_mirror(subtree1, subtree2):
        if subtree1 is None and subtree2 is None: return True
        if subtree1 is None or subtree2 is None: return False
        if not subtree1.data == subtree2.data: return False
        return is_mirror(subtree1.left, subtree2.right) and is_mirror(subtree1.right, subtree2.left)
    return is_mirror(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
