from test_framework import generic_test


def inorder_traversal(tree):
    if not tree:
        return []
    traversal, visited, stack = [], set(), [tree]
    while stack:
        curr = stack[-1]
        if curr.left and curr.left not in visited:
            stack.append(curr.left)
        else:
            traversal.append(curr.data)
            visited.add(stack.pop())
            if curr.right and curr.right not in visited: stack.append(curr.right)
    return traversal


def inorder_traversal_book(tree):
    stk, traversal = [], []
    while stk or tree:
        if tree:
            stk.append(tree)
            tree = tree.left    # Going left
        else:
            tree = stk.pop()    # Going up
            traversal.append(tree.data)
            tree = tree.right   # Going right
    return traversal

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
