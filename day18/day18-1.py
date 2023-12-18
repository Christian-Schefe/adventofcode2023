from collections import deque

DIRS = {'R': (1, 0), 'D': (0, 1), 'U': (0, -1), 'L': (-1, 0)}


def sign(num):
    return -1 if num < 0 else (1 if num > 0 else 0)


with open("input.txt") as f:
    lines = [x.strip().split(' ') for x in f.readlines()]
    vertices = [(0, 0)]

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for line in lines:
        last_vert = vertices[-1]
        dir = DIRS[line[0]]
        count = int(line[1])
        new_vert = (last_vert[0] + dir[0] * count, last_vert[1] + dir[1] * count)
        vertices.append(new_vert)
        max_x, max_y = max(max_x, new_vert[0]), max(max_y, new_vert[1])
        min_x, min_y = min(min_x, new_vert[0]), min(min_y, new_vert[1])

    straight_position_count = 0

    for i in range(1, len(vertices)):
        prev = vertices[i - 1]
        cur = vertices[i]
        dx, dy = sign(cur[0] - prev[0]), sign(cur[1] - prev[1])
        count = abs(cur[0] - prev[0]) + abs(cur[1] - prev[1])
        for i in range(count):
            pos = prev[0] + dx * i, prev[1] + dy * i
        straight_position_count += count - 1

    vertices.pop()

    area = 0

    vertices.insert(0, vertices[-1])
    vertices.append(vertices[1])
    print(vertices)

    for i in range(1, len(vertices) - 1):
        prev, cur, nxt = vertices[i - 1], vertices[i], vertices[i + 1]

        area += (cur[1] + nxt[1]) * (cur[0] - nxt[0])

    corner_area = 3 + (len(vertices) - 2 - 4) * 0.5
    straight_area = straight_position_count * 0.5

    print(area / 2)
    print(corner_area)
    print(straight_area)
    print(area / 2 + corner_area + straight_area)

    # for l in grid:
    #     print(''.join(l))
