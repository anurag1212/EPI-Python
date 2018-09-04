import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure

WHITE, GRAY, BLACK = range(3)


class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.color = WHITE


def clone_graph(graph):
    G = collections.OrderedDict()

    def dfs(curr):
        new_vertex = GraphVertex(None)
        if curr.color == GRAY:
            return
        else:
            new_vertex.label = curr.label
            G[curr.label] = new_vertex
        curr.color = GRAY
        for in_neighbor in curr.edges:
            new_vertex.edges.append(in_neighbor.label)
            if in_neighbor.color != BLACK:
                dfs(in_neighbor)
        curr.color = BLACK

    dfs(graph)
    for v in G:
        new_edges = list()
        for neighbor in G[v].edges:
            new_edges.append(G[neighbor])
        G[v].edges = new_edges

    start_vertex = G[graph.label]
    G = list(G.values())

    return start_vertex


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("graph_clone.py", 'graph_clone.tsv',
                                       clone_graph_test))
