enter_exit = {
    'F': {(0, -1): (1, 0), (-1, 0): (0, 1)},
    'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
    'L': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    '7': {(0, -1): (-1, 0), (1, 0): (0, 1)},
    '-': {(-1, 0): (-1, 0), (1, 0): (1, 0)},
    '|': {(0, -1): (0, -1), (0, 1): (0, 1)},
    '.': {},
    'S': {},
}


def find_loop(grid, start, dir):
    cur_pos = start
    cur_dir = dir
    steps = [cur_pos]
    while True:
        next_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])
        if next_pos[1] < 0 or next_pos[1] >= len(grid) or next_pos[0] < 0 or next_pos[0] >= len(grid[next_pos[1]]):
            return False

        next_tile = grid[next_pos[1]][next_pos[0]]

        if next_tile == 'S':
            return steps, (dir, cur_dir)
        next_dirs = enter_exit[next_tile]

        if cur_dir not in next_dirs:
            return False

        next_dir = next_dirs[cur_dir]

        cur_pos = next_pos
        cur_dir = next_dir
        steps.append(cur_pos)


with open("day10.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]
    grid = []

    start_pos = None

    for y, line in enumerate(lines):
        grid.append([])
        for x, tile in enumerate(line):
            if tile == 'S':
                start_pos = (x, y)
            grid[y].append(tile)
        # print(grid[y])

    print(start_pos)
    result = find_loop(grid, start_pos, (1, 0))
    if result == False:
        result = find_loop(grid, start_pos, (-1, 0))
    if result == False:
        result = find_loop(grid, start_pos, (0, 1))
    if result == False:
        result = find_loop(grid, start_pos, (0, -1))
    steps ,start_type = result
    print(steps)
    print(len(steps) / 2)
    inside_count = 0

    grid[start_pos[1]][start_pos[0]] = '|'

    for y, line in enumerate(grid):
        crossings = 0
        crossing_starter = None
        for x, tile in enumerate(line):
            if (x, y) in steps:
                if tile == '|':
                    crossings += 1
                elif crossing_starter == None and tile == 'F':
                    crossing_starter = 'F'
                elif crossing_starter == None and tile == 'L':
                    crossing_starter = 'L'

                elif crossing_starter == 'F' and tile == 'J':
                    crossings += 1
                    crossing_starter = None
                elif crossing_starter == 'F' and tile == '7':
                    crossing_starter = None

                elif crossing_starter == 'L' and tile == 'J':
                    crossing_starter = None
                elif crossing_starter == 'L' and tile == '7':
                    crossings += 1
                    crossing_starter = None

            elif crossings % 2 == 1:
                grid[y][x] = '#'
                inside_count += 1
            else:
                grid[y][x] = 'O'

            # grid[y][x] += ' ' if crossings % 2 == 0 else '_'

    for y in range(len(grid)):
        print(''.join(grid[y]))

    print(inside_count, start_type)