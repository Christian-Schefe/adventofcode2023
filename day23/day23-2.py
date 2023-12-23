from collections import deque, defaultdict
import sys

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sys.setrecursionlimit(100000)


def inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def is_walkable(x, y):
    return inside(x, y, w, h) and grid[y][x] != '#'


def follow(x, y, last_dx, last_dy):
    steps = 1
    while True:
        if not is_walkable(x, y):
            return None
        if (x, y) == (start, 0):
            return (x, y, steps)
        if (x, y) == (end, h - 1):
            return (x, y, steps)
        n = direct_neighbours(x, y)
        if len(n) >= 3:
            return (x, y, steps)
        if len(n) != 2:
            return None

        last_dx, last_dy = n[1][1] if n[0][1] == (-last_dx, -last_dy) else n[0][1]
        x += last_dx
        y += last_dy
        steps += 1


def direct_neighbours(x, y):
    return [((x + dx, y + dy), (dx, dy)) for dx, dy in DIRS if is_walkable(x + dx, y + dy)]


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    w, h = len(grid[0]), len(grid)
    start = grid[0].index('.')
    end = grid[-1].index('.')
    end_i = end + (h - 1) * w

    nodes = [(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile == '.' and len(direct_neighbours(x, y)) >= 3]
    nodes = [(x, y) for x, y in nodes if len(direct_neighbours(x, y)) >= 3]
    nodes.append((start, 0))
    nodes.append((end, h - 1))

    graph = {}
    for x, y in nodes:
        neighbours = [follow(x + dx, y + dy, dx, dy) for dx, dy in DIRS]
        graph[y * h + x] = [(n[1] * h + n[0], n[2]) for n in neighbours if n != None]

    print(graph)

    q = deque()
    q.appendleft(((start, ), 0))

    v = set()

    best_dist = 0

    while len(q) > 0:
        # print(best_dist, len(q))

        path, dist = q.pop()
        if path[-1] == end_i:
            if best_dist < dist:
                print(dist)
            best_dist = max(best_dist, dist)
            continue

        for n, d in graph[path[-1]]:
            if n in path:
                continue
            new_pos = (path + (n, ), dist + d)
            if new_pos in v:
                continue
            v.add(new_pos)
            q.appendleft(new_pos)


    # print(visited)
    print(best_dist)
