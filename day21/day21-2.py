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


def get_adj(x, y):
    q = set([((x, y), (0, 0))])
    for _ in range(1):
        nq = set()
        for (cx, cy), (lx, ly) in q:
            for dx, dy in DIRS:
                nx, ny = (cx + dx) % width, (cy + dy) % height
                nlx, nly = layer_offset(cx + dx, cy + dy)
                if grid[ny][nx] != '#':
                    nq.add(((nx, ny), (lx + nlx, ly + nly)))
        q = nq
    if ((x, y), (0, 0)) in q:
        q.remove(((x, y), (0, 0)))
    return list(q)


def get_distances(start):
    q = set([(start, (0, 0))])
    durations = {}
    max_dur = 0
    prev_durs = -1

    for i in range(0, width * height * 9):
        if len(durations) == prev_durs:
            break
        prev_durs = len(durations)
        nq = set()
        for pos, lpos in q:
            if (pos, lpos) not in durations:
                durations[(pos, lpos)] = i
                if lpos == (0, 0):
                    max_dur = max(max_dur, i)
                for ad, lad in adj[pos]:
                    if abs(lpos[0] + lad[0]) <= 1 and abs(lpos[1] + lad[1]) <= 1:
                        nq.add((ad, (lpos[0] + lad[0], lpos[1] + lad[1])))
        q = nq

    return durations, max_dur


with open("test.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    start_pos = [(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile == 'S'][0]
    width, height = len(grid[0]), len(grid)
    print(width, height, width * height)

    adj = {(x, y): get_adj(x, y) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile != '#'}

    durations, max_dur = get_distances(start_pos)

    evens = len([(x, y) for ((x, y), (lx, ly)), dur in durations.items() if (lx, ly) == (0, 0) and dur % 2 == 0])
    odds = len([(x, y) for ((x, y), (lx, ly)), dur in durations.items() if (lx, ly) == (0, 0) and dur % 2 == 1])

    nw_corner_durs, _ = get_distances((0, 0))
    ne_corner_durs, _ = get_distances((width - 1, 0))
    sw_corner_durs, _ = get_distances((0, height - 1))
    se_corner_durs, _ = get_distances((width - 1, height - 1))

    print("max dur:", max_dur)
    print("e/o:", evens, odds)

    reachable_count = 0
    STEPS = 26501365
    STEPS = 5000

    fully_inside_rings = (STEPS - max_dur) // width + 1

    even_ring_occs = 0
    odd_ring_occs = 0

    for i in range(fully_inside_rings):
        occs = max(1, 4 * i)
        if i % 2 == 0:
            even_ring_occs += occs
        else:
            odd_ring_occs += occs

    print(fully_inside_rings, even_ring_occs * evens, odd_ring_occs * odds)
    print(even_ring_occs * evens + odd_ring_occs * odds)

    outest_ring_s_steps = STEPS - fully_inside_rings * width
    outest_ring_se_corner_steps = STEPS - ((fully_inside_rings - 2) * width + durations[((0, 0), (0, 0))] + 2)
    outest_ring_occs = fully_inside_rings * 4

    print(outest_ring_s_steps, outest_ring_occs)
    print(outest_ring_se_corner_steps)
    print(outest_ring_se_corner_steps - nw_corner_durs[(start_pos, (0, 0))])
