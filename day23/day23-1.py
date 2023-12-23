from collections import deque, defaultdict

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SLOPES = ['>', 'v', '<', '^']
ANTI_SLOPES = ['<', '^', '>', 'v']


def inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def is_walkable(i, x, y):
    return inside(x, y, w, h) and grid[y][x] != '#' and grid[y][x] != ANTI_SLOPES[i]


def follow(x, y, path: list, last_dx, last_dy):
    while True:
        possible_dirs = [(i, dx, dy) for i, (dx, dy) in enumerate(DIRS) if is_walkable(x + dx, y + dy) and (dx, dy) != (last_dx, last_dy)]

        landing_pos = [(i, x + dx, y + dy) if grid[y + dy][x + dx] != SLOPES[i] else (i, x + 2 * dx, y + 2 * dy) for i, dx, dy in possible_dirs]
        landing_pos = [pos for pos in landing_pos if pos not in path]

        if len(landing_pos) == 0:
            return 0

        if len(landing_pos) == 1:
            path.append((x, y))
            i, x, y = landing_pos[0]
            last_dx, last_dy = DIRS[i]
            continue
        
        longest_path = 0
        path.append((x, y))
        for i, nx, ny in landing_pos:
            last_dx, last_dy = DIRS[i]
            path_len = follow(nx, ny, path.copy(), last_dx, last_dy)
            if path_len > longest_path:
                longest_path = path_len
        
        return longest_path


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start = grid[0].index('.')
    end = grid[-1].index('.')
    w, h = len(grid[0]), len(grid)
    q = deque()

    q.append((start, 0, [start]))

    visited = {start: 0}

    while len(q) > 0:
        x, y, path = q.pop()
        print(x, y)

        for i, (dx, dy) in enumerate(DIRS):
            nx, ny = x + dx, y + dy
            if not inside(nx, ny, w, h):
                continue
            if grid[ny][nx] == '#' or grid[ny][nx] == ANTI_SLOPES[i]:
                continue
            if grid[ny][nx] == SLOPES[i]:
                path = path + [(nx, ny)]
                nx, ny = nx + dx, ny + dy

            if (nx, ny) not in visited or visited[(nx, ny)] < len(path):
                if (nx, ny) not in path:
                    visited[(nx, ny)] = len(path)
                    q.append((nx, ny, path + [(nx, ny)]))

    print(visited)
    print(visited[(end, h - 1)] - 1)
