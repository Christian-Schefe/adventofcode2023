with open("day11.txt") as f:
    EXPANSION = 1_000_000
    lines = [x.strip() for x in f.readlines()]
    transposed = [[lines[y][x] for y in range(len(lines))] for x in range(len(lines[0]))]
    galaxies = [(x, y) for y, line in enumerate(lines) for x, tile in enumerate(line) if tile == "#"]

    cumulative_expansion_x, cumulative_expansion_y = [], []

    for y, line in enumerate(lines):
        cumulative_expansion_y.append(0 if y == 0 else cumulative_expansion_y[-1])
        if "#" not in line:
            cumulative_expansion_y[y] += 1

    for x, line in enumerate(transposed):
        cumulative_expansion_x.append(0 if x == 0 else cumulative_expansion_x[-1])
        if "#" not in line:
            cumulative_expansion_x[x] += 1

    dist_sum = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            min_x, max_x = min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])
            min_y, max_y = min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])
            expanded_cols = cumulative_expansion_x[max_x] - cumulative_expansion_x[min_x]
            expanded_rows = cumulative_expansion_y[max_y] - cumulative_expansion_y[min_y]
            dist_sum += max_x - min_x + max_y - min_y + (expanded_cols + expanded_rows) * (EXPANSION - 1)

    print(dist_sum)
