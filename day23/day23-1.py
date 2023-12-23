from collections import deque, defaultdict
import sys

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SLOPES = ['>', 'v', '<', '^']
ANTI_SLOPES = ['<', '^', '>', 'v']

sys.setrecursionlimit(100000)

def inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def is_walkable(i, x, y):
    return inside(x, y, w, h) and grid[y][x] != '#' and grid[y][x] != ANTI_SLOPES[i]


def follow(x, y, path: list, cache: dict):
    path.append((x, y))
    if x == end and y == h - 1:
        return len(path) - 1

    longest_path = 0

    for i, (dx, dy) in enumerate(DIRS):
        if not is_walkable(i, x + dx, y + dy):
            continue

        if grid[y][x] != '.' and grid[y][x] != SLOPES[i]:
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

    print(follow(start, 0, [], {}))
