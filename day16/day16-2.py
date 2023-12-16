def do_beam(grid, x, y, dx, dy, w, h, energized, done_splitters=set()):
    while True:
        x += dx
        y += dy

        if x < 0 or x >= w or y < 0 or y >= h:
            return

        energized[y][x] = 1

        if grid[y][x] == '/':
            dx, dy = -dy, -dx
        elif grid[y][x] == '\\':
            dx, dy = dy, dx
        elif grid[y][x] == '|' and dx != 0:
            if (x, y) not in done_splitters:
                done_splitters.add((x, y))
                do_beam(grid, x, y, 0, -1, w, h, energized, done_splitters)
                do_beam(grid, x, y, 0, 1, w, h, energized, done_splitters)
            return
        elif grid[y][x] == '-' and dy != 0:
            if (x, y) not in done_splitters:
                done_splitters.add((x, y))
                do_beam(grid, x, y, 1, 0, w, h, energized, done_splitters)
                do_beam(grid, x, y, -1, 0, w, h, energized, done_splitters)
            return


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    best_score, w, h = 0, len(grid[0]), len(grid)

    for y in range(h):
        energized = [[0 for _ in line] for line in grid]
        do_beam(grid, -1, y, 1, 0, w, h, energized, set())
        best_score = max(best_score, sum(map(sum, energized)))

        energized = [[0 for _ in line] for line in grid]
        do_beam(grid, w, y, -1, 0, w, h, energized, set())
        best_score = max(best_score, sum(map(sum, energized)))

    for x in range(w):
        energized = [[0 for _ in line] for line in grid]
        do_beam(grid, x, -1, 0, 1, w, h, energized, set())
        best_score = max(best_score, sum(map(sum, energized)))

        energized = [[0 for _ in line] for line in grid]
        do_beam(grid, x, h, 0, -1, w, h, energized, set())
        best_score = max(best_score, sum(map(sum, energized)))

    print(best_score)
