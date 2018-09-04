import functools
import collections

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


WHITE, GRAY, BLACK = range(3)


class GraphVertex:
    def __init__(self):
        self.color = WHITE
        self.edges = []


def is_deadlocked(graph):

    def has_cycle_dfs(curr):
        if curr.color == GRAY:
            return True

        curr.color = GRAY
        for neighbour in curr.edges:
            if neighbour.color != BLACK and has_cycle_dfs(neighbour):
                return True

        curr.color = BLACK
        return False

    for vertex in graph:
        if vertex.color == WHITE:
            if has_cycle_dfs(vertex):
                return True

    return False


def is_deadlocked_bfs(graph):

    def has_cycle_bfs(curr):
        q = collections.deque()
        q.append((curr, [curr]))
        while q:
            curr, path = q.popleft()
            for neighbor in curr.edges:
                if neighbor in path:
                    return True
                else:
                    q.append((neighbor, path + [neighbor]))
                    neighbor.color = GRAY
            curr.color = BLACK
        return False

    for vertex in graph:
        if vertex.color == WHITE:
            if has_cycle_bfs(vertex):
                return True

    return False


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
