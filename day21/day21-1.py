from collections import deque


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start_pos = [(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile == 'S'][0]
    width, height = len(grid[0]), len(grid)

    adj = {(x, y): [(x + dx, y + dy) for dx, dy in DIRS if is_inside(x + dx, y + dy, width, height) and grid[y + dy][x + dx] != '#']
           for y, line in enumerate(grid) for x, tile in enumerate(line) if tile != '#'}

    q = set([start_pos])

    for i in range(64):
        print(i, len(q))
        nq = set()
        for pos in q:
            for ad in adj[pos]:
                nq.add(ad)
        q = nq

    print(len(q))
