from test_framework import generic_test


def apply_permutation(perm, A):

    def follow_path(i):
        new_index = perm[i]
        perm[i] = None
        temp = A[i]
        while new_index is not None:
            A[new_index], temp = temp, A[new_index]  # Replace to new position
            i = new_index        # Move forward in path
            new_index = perm[i]  # Update new_index
            perm[i] = None       # Signify that he doesn't need to move
        return

    perm_index = 0
    while perm_index < len(A):
        follow_path(perm_index)
        while perm_index < len(A) and perm[perm_index] is None:
            perm_index += 1
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
