from test_framework import generic_test
import collections


def fill_surrounded_regions(board):
    WHITE, BLACK, connected_tiles, MAX_ROWS , MAX_COLS = "W", "B", set(), len(board), len(board[0])

    def connected_regions(x, y, flip=False):
        q, visited = collections.deque(), set()
        q.append((x, y))
        while q:
            curr_x, curr_y = q.popleft()
            visited.add((curr_x, curr_y))
            if flip:
                board[curr_x][curr_y] = BLACK
            else:
                connected_tiles.add((curr_x, curr_y))
            for neighbor in ((curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)):
                if 0 <= neighbor[0] < MAX_ROWS and 0 <= neighbor[1] < MAX_COLS and board[neighbor[0]][neighbor[1]] == WHITE and neighbor not in visited:
                    q.append(neighbor)

    for j in range(MAX_COLS - 1):
        if board[0][j] == WHITE and (0, j) not in connected_tiles:
            connected_regions(0, j)
    for i in range(MAX_ROWS - 1):
        if board[i][MAX_COLS - 1] == WHITE and (i, MAX_COLS - 1) not in connected_tiles:
            connected_regions(i, MAX_COLS - 1)
    for j in range(MAX_COLS - 1, 0, -1):
        if board[MAX_ROWS - 1][j] == WHITE and (MAX_ROWS - 1, j) not in connected_tiles:
            connected_regions(MAX_ROWS - 1, j)
    for i in range(MAX_ROWS - 1, 0, -1):
        if board[i][0] == WHITE and (i, 0) not in connected_tiles:
            connected_regions(i, 0)

    for i in range(1, MAX_ROWS-1):
        for j in range(1, MAX_COLS-1):
            if board[i][j] == WHITE and (i, j) not in connected_tiles:
                # connected_regions(i, j, flip=True) # For inputs with huge internal whites, this is a waste
                board[i][j] = BLACK

    return board


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
