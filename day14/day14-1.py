def load(field):
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

    loads = [0 for _ in square_rocks]
    for i, pos in enumerate(square_rocks):
        for y in range(1, rock_counts[i] + 1):
            loads[i] += len(field) - (pos[1] + y)

    return sum(loads)


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


    field = do_move(field, 0)
    loads = load(field)
    print(loads)