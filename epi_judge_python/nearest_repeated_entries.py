from test_framework import generic_test


def find_nearest_repetition(paragraph):
    dist, visited = float('inf'), dict()
    for i, word in enumerate(paragraph):
        if word in visited:
            dist = min(dist, i - visited[word])
        visited[word] = i
    return -1 if dist == float('inf') else dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
