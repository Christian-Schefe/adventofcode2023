def do_beam(grid, x, y, dx, dy, w, h, energized, done_splitters):
    cx, cy = x, y

    while True:
        cx += dx
        cy += dy

        if cx < 0 or cx >= w or cy < 0 or cy >= h:
            break

        energized[cy][cx] = 1

        if grid[cy][cx] == '/':
            if dx == 1:
                dx, dy = 0, -1
            elif dx == -1:
                dx, dy = 0, 1
            elif dy == 1:
                dx, dy = -1, 0
            elif dy == -1:
                dx, dy = 1, 0
        elif grid[cy][cx] == '\\':
            if dx == 1:
                dx, dy = 0, 1
            elif dx == -1:
                dx, dy = 0, -1
            elif dy == 1:
                dx, dy = 1, 0
            elif dy == -1:
                dx, dy = -1, 0
        elif (cx, cy) not in done_splitters and grid[cy][cx] == '|' and dx != 0:
            done_splitters.add((cx, cy))
            energized, done_splitters = do_beam(grid, cx, cy, 0, -1, w, h, energized, done_splitters)
            energized, done_splitters = do_beam(grid, cx, cy, 0, 1, w, h, energized, done_splitters)
            break
            # dx, dy = 0, 1
        elif (cx, cy) not in done_splitters and grid[cy][cx] == '-' and dy != 0:
            done_splitters.add((cx, cy))
            energized, done_splitters = do_beam(grid, cx, cy, 1, 0, w, h, energized, done_splitters)
            energized, done_splitters = do_beam(grid, cx, cy, -1, 0, w, h, energized, done_splitters)
            break
            # dx, dy = -1, 0

    return energized, done_splitters


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    energized = [[0 for _ in line] for line in grid]
    done_splitters = set()
    energized, done_splitters = do_beam(grid, -1, 0, 1, 0, len(grid[0]), len(grid), energized, done_splitters)
    for l in energized:
        print("".join(['#' if x == 1 else '.' for x in l]))
    print(sum([sum(x) for x in energized]))
