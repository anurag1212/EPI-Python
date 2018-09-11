import functools
import collections

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

WHITE, GRAY, BLACK = range(3)


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []
        self.color = WHITE
        self.side = None


def is_any_placement_feasible(graph):

    def bfs(start):
        q, start.side, start.color = collections.deque(), True, GRAY
        q.append(start)
        while q:
            curr = q.popleft()
            for neighbor in curr.edges:
                if neighbor.color == WHITE:
                    neighbor.side, neighbor.color = not curr.side, GRAY
                    q.append(neighbor)
                elif neighbor.side == curr.side:
                    return True
            curr.color = BLACK

    left, right = [], []
    cycle = any([bfs(v) for v in graph if v.color == WHITE])
    for v in graph:
        left.append(graph.index(v)) if v.side else right.append(graph.index(v))
    return not cycle


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
