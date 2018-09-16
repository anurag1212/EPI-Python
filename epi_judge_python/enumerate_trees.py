import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def generate_all_binary_trees(num_nodes):
    if not num_nodes:
        return [[0]]
    tree = [0 for _ in range(2**num_nodes-1)]
    tree[0] = 1
    trees = []

    def gen_trees(root, parent, n):
        if n==0:
            trees.append(list(tree))
            return
        l = root * 2 + 1
        r = root * 2 + 2
        tree[l] = 1
        gen_trees(l, root, n-1)
        tree[l] = 0
        tree[r] = 1
        gen_trees(r, root, n-1)
        tree[r] = 0
        if n>1:
            tree[l] = tree[r] = 1
            gen_trees(l, root, n-2)
            if n-2 > 0:
                gen_trees(r, root, n-2)
            tree[l] = tree[r] = 0

    gen_trees(0, 0, num_nodes-1)

    return trees


for a in generate_all_binary_trees(3): print(a)
for a in generate_all_binary_trees(4): print(a)

# def serialize_structure(tree):
#     result = []
#     q = [tree]
#     while q:
#         a = q.pop(0)
#         result.append(0 if not a else 1)
#         if a:
#             q.append(a.left)
#             q.append(a.right)
#     return result
#
#
# @enable_executor_hook
# def generate_all_binary_trees_wrapper(executor, num_nodes):
#     result = executor.run(
#         functools.partial(generate_all_binary_trees, num_nodes))
#
#     return sorted(map(serialize_structure, result))
#
#
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("enumerate_trees.py",
#                                        'enumerate_trees.tsv',
#                                        generate_all_binary_trees_wrapper))
