from test_framework import generic_test


def get_int(string):
    res = 0
    if string:
        res = int(string, base=2)
    return res


def sum_root_to_leaf(tree, path=[]):
    if not tree: return 0
    partial_path_sum = 0
    path.append(str(tree.data))
    if not tree.left and not tree.right:
        partial_path_sum += get_int(''.join(path))
    if tree.left:
        partial_path_sum += sum_root_to_leaf(tree.left, path)
    if tree.right:
        partial_path_sum += sum_root_to_leaf(tree.right, path)
    path.pop()
    return partial_path_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
