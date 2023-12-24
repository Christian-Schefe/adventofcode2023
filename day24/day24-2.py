from collections import deque, defaultdict

MIN_POS = 200_000_000_000_000
# MIN_POS = 7
MAX_POS = 400_000_000_000_000
# MAX_POS = 27


def test_intersect(pos_a, vel_a, pos_b, vel_b):
    m_a = vel_a[1] / vel_a[0]
    b_a = pos_a[1] - m_a * pos_a[0]

    m_b = vel_b[1] / vel_b[0]
    b_b = pos_b[1] - m_b * pos_b[0]

    if (m_b - m_a) == 0:
        return None

    ix = (b_a - b_b) / (m_b - m_a)
    iy = b_a + m_a * ix

    if (vel_a[0] >= 0 and ix < pos_a[0]) or (vel_a[0] < 0 and ix > pos_a[0]):
        return None
    if (vel_b[0] >= 0 and ix < pos_b[0]) or (vel_b[0] < 0 and ix > pos_b[0]):
        return None

    return (ix, iy)


with open("input.txt") as f:
    positions, velocities = list(zip(*[x.strip().split('@') for x in f.readlines()]))
    stone_count = len(positions)
    positions = [tuple(map(int, pos.split(','))) for pos in positions]
    velocities = [tuple(map(int, vel.split(','))) for vel in velocities]
    print(positions, velocities)

    within_bounds = 0

    for i in range(stone_count - 1):
        for j in range(i + 1, stone_count):
            res = test_intersect(positions[i], velocities[i], positions[j], velocities[j])
            if res is None:
                continue
            x, y = res
            if x >= MIN_POS and y >= MIN_POS and x <= MAX_POS and y <= MAX_POS:
                within_bounds += 1
            print(x, y)
    print(within_bounds)