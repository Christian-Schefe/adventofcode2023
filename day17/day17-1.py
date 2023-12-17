from collections import deque


def is_inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def get_targets(x, y, dx, dy, heat, w, h, grid):
    targets = []
    heat_cum = heat
    best_end_heat = 999999
    for i in range(3):
        nx, ny = x + i * dx, y + i * dy
        if not is_inside(nx, ny, w, h):
            break
        if i > 0:
            heat_cum += grid[ny][nx]

        if (nx, ny) == (w - 1, h - 1):
            best_end_heat = min(best_end_heat, heat_cum)

        if is_inside(nx + dy, ny + dx, w, h):
            if (nx + dy, ny + dx) == (w - 1, h - 1):
                best_end_heat = min(best_end_heat, heat_cum + grid[ny + dx][nx + dy])
            targets.append((nx + dy, ny + dx, dy, dx, heat_cum + grid[ny + dx][nx + dy]))
        if is_inside(nx - dy, ny - dx, w, h):
            if (nx - dy, ny - dx) == (w - 1, h - 1):
                best_end_heat = min(best_end_heat, heat_cum + grid[ny - dx][nx - dy])
            targets.append((nx - dy, ny - dx, -dy, -dx, heat_cum + grid[ny - dx][nx - dy]))

    return targets, best_end_heat


with open("test.txt") as f:
    grid = [list(map(int, list(x.strip()))) for x in f.readlines()]
    w, h = len(grid[0]), len(grid)

    q = deque()
    q.extend(get_targets(0, 0, 1, 0, 0, w, h, grid)[0])
    q.extend(get_targets(0, 0, 0, 1, 0, w, h, grid)[0])

    best_end_heat = 999999

    visited = {}

    while len(q) > 0:
        x, y, dx, dy, heat = q.pop()
        if (x, y) == (w - 1, h - 1):
            print(x, y, dx, dy, heat)

        tar, end_heat = get_targets(x, y, dx, dy, heat, w, h, grid)
        best_end_heat = min(best_end_heat, end_heat)

        for t in tar:
            key = t[:4]
            if key not in visited or visited[key] > t[-1]:
                q.appendleft(t)
                visited[key] = t[-1]

    print(best_end_heat)
