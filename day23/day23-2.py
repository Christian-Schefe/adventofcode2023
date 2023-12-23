from collections import deque, defaultdict
import sys

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SLOPES = ['>', 'v', '<', '^']
ANTI_SLOPES = ['<', '^', '>', 'v']

sys.setrecursionlimit(100000)

def inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def is_walkable(i, x, y):
    return inside(x, y, w, h) and grid[y][x] != '#'


def follow(x, y, path: list, cache: dict):
    path.append((x, y))
    if x == end and y == h - 1:
        print(len(path) - 1)
        return len(path) - 1

    longest_path = 0

    for i, (dx, dy) in enumerate(DIRS):
        if not is_walkable(i, x + dx, y + dy):
            continue

        if (x + dx, y + dy) in path:
            continue

        longest_path = max(longest_path, follow(x + dx, y + dy, path.copy(), cache))

    return longest_path



with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start = grid[0].index('.')
    end = grid[-1].index('.')
    w, h = len(grid[0]), len(grid)

    # print(follow(start, 0, [], {}))

    q = deque()

    q.append((start, 0, [start]))

    visited = set()
    visited.add((start, 0, 1))

    best_dist = 0

    while len(q) > 0:
        x, y, path = q.pop()
        # print(x, y)
        if x == end and y == h - 1:
            print(len(path))
            best_dist = max(best_dist, len(path))

        for i, (dx, dy) in enumerate(DIRS):
            nx, ny = x + dx, y + dy
            if not is_walkable(i, nx, ny):
                continue

            if (nx, ny) in path:
                continue

            if (nx, ny, tuple(path)) not in visited:
                visited.add((nx, ny, tuple(path)))
                q.append((nx, ny, path + [(nx, ny)]))

    # print(visited)
    print(best_dist - 1)
