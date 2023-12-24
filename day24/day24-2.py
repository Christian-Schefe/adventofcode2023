from collections import deque, defaultdict

MIN_POS = 200_000_000_000_000
# MIN_POS = 7
MAX_POS = 400_000_000_000_000
# MAX_POS = 27

def cal():
    pass


def get_pos(p, v, t):
    return (p[0] + t * v[0], p[1] + t * v[1], p[2] + t * v[2])


def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])


def sub(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def div(p1, n):
    return (p1[0] / n, p1[1] / n, p1[2] / n)


def mul(p1, n):
    return (p1[0] * n, p1[1] * n, p1[2] * n)


def is_int(p1):
    return p1[0] == int(p1[0]) and p1[1] == int(p1[1]) and p1[2] == int(p1[2])


def is_inside(p1):
    return p1[0] >= MIN_POS and p1[0] <= MAX_POS and p1[1] >= MIN_POS and p1[1] <= MAX_POS and p1[2] >= MIN_POS and p1[2] <= MAX_POS


def test_intersect(p1, v1, p2, v2):
    # p1 + t * v1 == p2 + t * v2
    # t * v1 - t * v2 == p2 - p1
    # t == (p2 - p1) / (v1 - v2)
    ts = []
    if v1[0] == v2[0]:
        if p1[0] != p2[0]:
            return None
    else:
        ts.append((p2[0] - p1[0]) / (v1[0] - v2[0]))

    if v1[1] == v2[1]:
        if p1[1] != p2[1]:
            return None
    else:
        ts.append((p2[1] - p1[1]) / (v1[1] - v2[1]))

    if v1[2] == v2[2]:
        if p1[2] != p2[2]:
            return None
    else:
        ts.append((p2[2] - p1[2]) / (v1[2] - v2[2]))

    # print(p1, v1, p2, v2, ts)
    for i in range(len(ts)):
        if ts[i] != ts[0]:
            return None

    if len(ts) == 0:
        return True

    t = ts[0]
    if t < 0:
        return None

    pos = get_pos(p1, v1, t)
    pos2 = get_pos(p2, v2, t)
    # print(pos, pos2)
    return pos


def step(old_positions):
    new_positions = [add(pos, vel) for pos, vel in zip(old_positions, velocities)]
    return new_positions


with open("input.txt") as f:
    positions, velocities = list(zip(*[x.strip().split('@') for x in f.readlines()]))
    positions = [tuple(map(int, pos.split(','))) for pos in positions]
    velocities = [tuple(map(int, vel.split(','))) for vel in velocities]
    stone_count = len(positions)

    for i in range(stone_count):
        for j in range(stone_count):
            if i == j:
                continue
            for t in range(10000):
                if t % 100 == 0:
                    print("->", i, j, t)
                first_hit_pos = get_pos(positions[i], velocities[i], t)
                if not is_inside(first_hit_pos):
                    continue
                for t2 in range(1, 10000):
                    second_hit_pos = get_pos(positions[j], velocities[j], t + t2)
                    if not is_inside(second_hit_pos):
                        continue
                    stone_vel = div(sub(second_hit_pos, first_hit_pos), t2)
                    stone_pos = sub(first_hit_pos, mul(stone_vel, t))
                    if not is_int(stone_vel):
                        continue
                    if not is_inside(stone_pos):
                        continue
                        # print(t, t2, stone_pos, first_hit_pos, stone_vel)

                    for k in range(stone_count):
                        if k == i or k == j:
                            continue
                        res = test_intersect(stone_pos, stone_vel, positions[k], velocities[k])
                        if res is None:
                            break
                        if not is_inside(stone_pos):
                            break
                    else:
                        print(stone_pos)
                        print(stone_pos[0] + stone_pos[1] + stone_pos[2])
                        exit()
