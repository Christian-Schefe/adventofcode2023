def load(rock_pos, height):
    return sum([height - pos[1] for pos in rock_pos])


def do_move(field, direc):
    for _ in range(direc):
        field = [[field[x][len(field) - y - 1] for x in range(len(line))] for y, line in enumerate(field)]

    square_rocks = [(x, -1) for x in range(len(field[0]))] + [(x, y) for y, line in enumerate(field) for x, tile in enumerate(line) if tile == '#']
    rock_counts = [0 for _ in square_rocks]

    for i, pos in enumerate(square_rocks):
        for y in range(1, len(field) + 1):
            if pos[1] + y >= len(field):
                break
            if field[pos[1] + y][pos[0]] == '#':
                break
            if field[pos[1] + y][pos[0]] == 'O':
                rock_counts[i] += 1

    for i, pos in enumerate(square_rocks):
        for y in range(1, len(field) + 1):
            if pos[1] + y >= len(field):
                break
            if field[pos[1] + y][pos[0]] == '#':
                break
            field[pos[1] + y][pos[0]] = 'O' if y <= rock_counts[i] else '.'

    for _ in range(4 - direc):
        field = [[field[x][len(field) - y - 1] for x in range(len(line))] for y, line in enumerate(field)]

    return field


with open("input.txt") as f:
    field = [list(x.strip()) for x in f.readlines()]
    width = len(field[0])
    height = len(field)
    visited = {}
    first_rep = None
    loop_len = 0
    loop_offset = 0
    loads = []

    for i in range(1_000_000_000):
        rock_pos = tuple((x, y) for y in range(height) for x in range(width) if field[y][x] == 'O')
        loads.append(load(rock_pos, height))
        for j in [0, 3, 2, 1]:
            field = do_move(field, j)

        if rock_pos in visited:
            print(rock_pos)
            loop_len = i - visited[rock_pos]
            loop_offset = visited[rock_pos]
            break
        else:
            visited[rock_pos] = i

    load_index = loop_offset + ((1_000_000_000 - loop_offset) % loop_len)
    print(load_index, loads)
    print(loads[load_index])
