from collections import deque


def is_inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


with open("test.txt") as f:
    grid = [list(map(int, list(x.strip()))) for x in f.readlines()]
    width = len(grid[0])
    height = len(grid)
    best_heat = [[float('inf') for _ in range(width)] for _ in range(height)]

    queue = deque()
    queue.append((1, 0, (1, 0), 2, grid[0][1]))
    queue.append((0, 1, (0, 1), 2, grid[1][0]))

    best_heat[0][1] = grid[0][1]
    best_heat[1][0] = grid[1][0]

    visited = set()

    while len(queue) > 0:
        # print(len(queue))
        x, y, (dx, dy), moves_left, heat = queue.pop()

        if (x, y) == (5, 1):
            print(x, y, (dx, dy), moves_left, heat)

        if is_inside(x + dx, y + dy, width, height) and moves_left > 0:
            nx, ny = x + dx, y + dy
            new_heat = heat + grid[ny][nx]
            v1 = (nx, ny, (dx, dy), moves_left - 1, new_heat)

            if v1[:4] not in visited or new_heat < best_heat[ny][nx]:
                queue.appendleft(v1)
                visited.add(v1[:4])

            best_heat[ny][nx] = min(best_heat[ny][nx], new_heat)

        if is_inside(x + dy, y + dx, width, height):
            nx, ny = x + dy, y + dx
            new_heat = heat + grid[ny][nx]
            v2 = (nx, ny, (dy, dx), 3, new_heat)

            if v2[:4] not in visited or new_heat < best_heat[ny][nx]:
                queue.appendleft(v2)
                visited.add(v2[:4])

            best_heat[ny][nx] = min(best_heat[ny][nx], new_heat)

        if is_inside(x - dy, y - dx, width, height):
            nx, ny = x - dy, y - dx
            new_heat = heat + grid[ny][nx]
            v3 = (nx, ny, (-dy, -dx), 3, new_heat)

            if v3[:4] not in visited or new_heat < best_heat[ny][nx]:
                queue.appendleft(v3)
                visited.add(v3[:4])

            best_heat[ny][nx] = min(best_heat[ny][nx], new_heat)

    for l in best_heat:
        print(l)

    print(best_heat[height - 1][width - 1])
