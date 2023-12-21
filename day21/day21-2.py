from collections import deque


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def layer_offset(x, y):
    lx, ly = 0, 0
    if x < 0:
        lx = -1
    elif x >= width:
        lx = 1
    if y < 0:
        ly = -1
    elif y >= height:
        ly = 1

    return lx, ly


def is_inside(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h


def get_adj(x, y):
    adj = [(x + dx, y + dy) for dx, dy in DIRS if is_inside(x + dx, y + dy, width, height) and grid[y + dy][x + dx] != '#']
    return adj


def get_distances(start):
    q = set([start])
    durations = {}
    max_dur = 0
    prev_durs = -1

    for i in range(0, width * height):
        if len(durations) == prev_durs:
            break
        prev_durs = len(durations)
        nq = set()
        for pos in q:
            if pos not in durations:
                durations[pos] = i
                max_dur = max(max_dur, i)
                for ad in adj[pos]:
                    nq.add(ad)
        q = nq

    return durations, max_dur


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start_pos = [(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile == 'S'][0]
    width, height = len(grid[0]), len(grid)
    print(width, height, width * height)

    adj = {(x, y): get_adj(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile != '#'}

    reachable_count = 0
    STEPS = 26501365
    # STEPS = 5000

    CORNERS = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
    EDGES = [(start_pos[0], 0), (start_pos[0], height - 1), (0, start_pos[1]), (width - 1, start_pos[1])]

    center_durs = get_distances(start_pos)
    corner_durs = [get_distances(corner) for corner in CORNERS]
    edge_durs = [get_distances(edge) for edge in EDGES]

    i = 0
    while True:
        center_occs = 1 if i == 0 else 0
        corner_occs = 0 if i <= 1 else i - 1
        edge_occs = 0 if i == 0 else 1

        center_steps_left = STEPS - (i * width) 
        corner_steps_left = STEPS - ((i - 2) * width + width + 1)
        edge_steps_left = STEPS - ((i - 1) * width + (width + 1) // 2)

        print(i, center_occs, corner_occs, edge_occs)
        print(i, center_steps_left, corner_steps_left, edge_steps_left)
        old_count = reachable_count

        if center_occs > 0 and center_steps_left >= 0:
            center_reachables = [(x, y) for (x, y), dur in center_durs[0].items() if center_steps_left >= dur and (center_steps_left - dur) % 2 == 0]
            reachable_count += center_occs * len(center_reachables)

        if corner_occs > 0 and corner_steps_left >= 0:
            for durs in corner_durs:
                corner_reachables = [(x, y) for (x, y), dur in durs[0].items() if corner_steps_left >= dur and (corner_steps_left - dur) % 2 == 0]
                reachable_count += corner_occs * len(corner_reachables)

        if edge_occs > 0 and edge_steps_left >= 0:
            for durs in edge_durs:
                edge_reachables = [(x, y) for (x, y), dur in durs[0].items() if edge_steps_left >= dur and (edge_steps_left - dur) % 2 == 0]
                reachable_count += edge_occs * len(edge_reachables)

        if old_count == reachable_count:
            break
        i += 1

    print(reachable_count)