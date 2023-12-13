from collections import Counter
from math import lcm

with open("day8.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    route = lines.pop(0)
    lines.pop(0)
    table = {line.split(' ')[0]: (line.split('(')[1][0:3], line.split(' ')[3][0:3]) for line in lines}
    print(route, table)


    cursa = [key for key in table if key[2] == 'A']
    lcms = []
    for val in cursa:
        ri = 0
        curs = [val]

        while True:
            i = 0 if route[ri % len(route)] == 'L' else 1
            curs = [table[cur][i] for cur in curs]
            ri += 1
            if ri % 100000 == 0:
                print(ri)
            finished = True
            for cur in curs:
                if cur[2] != 'Z':
                    finished = False
                    break
            if finished:
                break
        lcms.append(ri)

    print(lcms, cursa, len(route))
    print([a % len(route) for a in lcms])
    print(lcm(*lcms))
