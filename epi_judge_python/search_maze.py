import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):

    # print(maze, s, e)

    # start 11:40
    # end 12:11

    G = collections.defaultdict(list)
    MAX_ROWS = len(maze)
    MAX_COLS = len(maze[0])
    print(MAX_ROWS, MAX_COLS)

    def make_adjacency_list(m):

        def add_adjacents(i, j):

            def satisfies_constraints(dir):
                row, col = dir[0], dir[1]
                return False if row >= MAX_ROWS or row < 0 or col >= MAX_COLS or col < 0 else True

            UP = (i-1, j)
            DOWN = (i+1, j)
            LEFT = (i, j-1)
            RIGHT = (i, j+1)
            directions = [UP, DOWN, LEFT, RIGHT]
            for direction in directions:
                if satisfies_constraints(direction) and m[direction[0]][direction[1]] != BLACK:
                    G[Coordinate(i, j)].append(Coordinate(direction[0], direction[1]))

        for i in range(MAX_ROWS-1, -1, -1):
            for j in range(MAX_COLS):
                if m[i][j] != BLACK:
                    add_adjacents(i, j)

    make_adjacency_list(maze)

    def bfs_shortest_path(g, start, end):
        q, visited = collections.deque(), set()
        q.append((start, [start]))
        while q:
            curr, path = q.popleft()
            visited.add(curr)
            if curr == end:
                return path
            else:
                for next_cell in (set(g[curr]) - set(path)) - visited:
                    q.append((next_cell, path + [next_cell]))
        return []

    def bfs_shortest_path_new(g, start, end):

        def traverse_path():
            walker, path = end, list()
            while walker != -1:
                path.append(walker)
                walker = meta[walker][1]
            return list(reversed(path))

        q = collections.deque()
        q.append(start)
        meta = {Coordinate(i, j): [float('inf'), None] for j in range(MAX_COLS) for i in range(MAX_ROWS)}
        meta[start] = [0, -1]
        while q:
            curr = q.popleft()
            if curr == end:
                return traverse_path()
            else:
                for neighbour in g[curr]:
                    feasible_distance = meta[curr][0] + 1
                    if feasible_distance < meta[neighbour][0]:
                        meta[neighbour][0] = feasible_distance
                        meta[neighbour][1] = curr
                        q.append(neighbour)
        return []

    return bfs_shortest_path(G, s, e)
    # return bfs_shortest_path_new(G, s, e)


# m = [[0,0,0,1],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
# s = Coordinate(1,0)
# e = Coordinate(1,3)

# m = [[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
# s = Coordinate(1,1)
# e = Coordinate(1,4)
# print(search_maze(m, s, e))


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
