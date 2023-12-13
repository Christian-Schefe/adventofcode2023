from collections import Counter

with open("day11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

    expanded = []
    for line in lines:
        expanded.append(line)
        if '#' not in line:
            expanded.append(line)
    transposed = [[expanded[y][x] for y in range(len(expanded))] for x in range(len(expanded[0]))]
    expanded = []
    
    for line in transposed:
        expanded.append(line)
        if '#' not in line:
            expanded.append(line)
    
    
    transposed = [[expanded[y][x] for y in range(len(expanded))] for x in range(len(expanded[0]))]

    galaxies = []
    for y, line in enumerate(transposed):
        for x, tile in enumerate(line):
            if tile == '#':
                galaxies.append((x, y))
    
    dist_sum = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dist_sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

    print(dist_sum)
