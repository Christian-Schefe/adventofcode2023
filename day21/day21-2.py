from collections import deque


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_inside(x, y):
    return x >= 0 and y >= 0 and x < width and y < height


def get_adj(x, y):
    return [(x + dx, y + dy) for dx, dy in DIRS if is_inside(x + dx, y + dy) and grid[y + dy][x + dx] != '#']


def get_distances(start):
    q = set([start])
    durations = {}
    prev_durs = -1

    for i in range(0, width * height):
        if len(durations) == prev_durs:
            break
        prev_durs = len(durations)
        nq = set()
        for pos in q:
            if pos not in durations:
                durations[pos] = i
                for ad in adj[pos]:
                    nq.add(ad)
        q = nq

    return durations


with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start_pos = [(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile == 'S'][0]
    width, height = len(grid[0]), len(grid)

    adj = {(x, y): get_adj(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile != '#'}

    STEPS = 26501365

    CORNERS = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
    EDGES = [(start_pos[0], 0), (start_pos[0], height - 1), (0, start_pos[1]), (width - 1, start_pos[1])]

    center_durs = get_distances(start_pos)
    max_dur_from_center = max(center_durs.values())
    corner_durs = [get_distances(corner) for corner in CORNERS]
    edge_durs = [get_distances(edge) for edge in EDGES]

    evens = len([1 for _, dur in center_durs.items() if (dur % 2) == 0])
    odds = len([1 for _, dur in center_durs.items() if (dur % 2) != 0])

    i = 0
    reachable_count = 0
    while True:
        center_occs = 1 if i == 0 else 0
        corner_occs = 0 if i <= 1 else i - 1
        edge_occs = 0 if i == 0 else 1

        center_steps_left = STEPS - (i * width)
        corner_steps_left = STEPS - ((i - 2) * width + width + 1)
        edge_steps_left = STEPS - ((i - 1) * width + (width + 1) // 2)

        old_count = reachable_count

        if center_steps_left >= max_dur_from_center:
            reachables = evens if (center_steps_left % 2) == 0 else odds
            if center_occs > 0 and center_steps_left >= 0:
                reachable_count += center_occs * reachables

            if corner_occs > 0 and corner_steps_left >= 0:
                reachable_count += len(corner_durs) * corner_occs * reachables

            if edge_occs > 0 and edge_steps_left >= 0:
                reachable_count += len(edge_durs) * edge_occs * reachables

        else:
            if center_occs > 0 and center_steps_left >= 0:
                center_reachables = [(x, y) for (x, y), dur in center_durs.items() if center_steps_left >= dur and (center_steps_left - dur) % 2 == 0]
                reachable_count += center_occs * len(center_reachables)

            if corner_occs > 0 and corner_steps_left >= 0:
                for durs in corner_durs:
                    corner_reachables = [(x, y) for (x, y), dur in durs.items() if corner_steps_left >= dur and (corner_steps_left - dur) % 2 == 0]
                    reachable_count += corner_occs * len(corner_reachables)

            if edge_occs > 0 and edge_steps_left >= 0:
                for durs in edge_durs:
                    edge_reachables = [(x, y) for (x, y), dur in durs.items() if edge_steps_left >= dur and (edge_steps_left - dur) % 2 == 0]
                    reachable_count += edge_occs * len(edge_reachables)

        if old_count == reachable_count:
            break

        i += 1

    print(reachable_count)
