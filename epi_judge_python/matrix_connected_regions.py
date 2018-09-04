from test_framework import generic_test
import collections

def flip_color(x, y, image):
    # Start : 12:04

    NEW_COLOR = not image[x][y]

    MAX_ROWS = len(image)
    MAX_COLS = len(image[0])

    def get_neighbors(cell):

        neighbors = list()

        def is_valid(neighbor):
            return False if (neighbor[0] < 0 or neighbor[0] >= MAX_ROWS or neighbor[1] < 0 or neighbor[1] >= MAX_COLS) else True

        directions = [(cell[0]-1, cell[1]),
                      (cell[0]+1, cell[1]),
                      (cell[0], cell[1]-1),
                      (cell[0], cell[1]+1)]

        for direction in [d for d in directions if is_valid(d)]:
            if bool(image[direction[0]][direction[1]] ^ image[cell[0]][cell[1]]):
                neighbors.append(direction)

        return neighbors

    def bfs(s):
        visited, queue = set(), collections.deque()
        queue.append(s)
        while queue:
            curr = queue.popleft()
            if curr not in visited:
                image[curr[0]][curr[1]] ^= 1
                visited.add(curr)
                for next_cell in get_neighbors(curr):  # - set(curr): should work but doesn't
                    if next_cell not in visited:
                        queue.append(next_cell)        # Add valid neighbors to queue

    bfs((x, y))

    return image


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
