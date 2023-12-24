from collections import deque, defaultdict
from math import lcm, gcd


def get_intersect(pos_a, vel_a, pos_b, vel_b):
    res = get_any_intersect(pos_a, vel_a, pos_b, vel_b)
    if res == None:
        return None
    ret, mua, mub = res
    if mua != int(mua) or int(mua) != int(mub):
        return None
    if int(mua) < 0:
        return None

    return ret


def get_any_intersect(pos_a, vel_a, pos_b, vel_b):
    p1, p2, p3, p4 = pos_a, add(pos_a, vel_a), pos_b, add(pos_b, vel_b)

    divisor = (dot2(p2, p1, p2, p1) * dot2(p4, p3, p4, p3) - dot2(p4, p3, p2, p1) * dot2(p4, p3, p2, p1))
    if divisor == 0:
        return None,
    mua = (dot2(p1, p3, p4, p3) * dot2(p4, p3, p2, p1) - dot2(p1, p3, p2, p1) * dot2(p4, p3, p4, p3)) / divisor
    mub = (dot2(p1, p3, p4, p3) + mua * dot2(p4, p3, p2, p1)) / dot2(p4, p3, p4, p3)

    return add(pos_a, mul(vel_a, int(mua))), mua, mub


def get_pos(p, v, t):
    return (p[0] + t * v[0], p[1] + t * v[1], p[2] + t * v[2])


def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])


def sub(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def div(p1, n):
    return (p1[0] / n, p1[1] / n, p1[2] / n)


def int_div(p1, n):
    return (p1[0] // n, p1[1] // n, p1[2] // n)


def mul(p1, n):
    return (p1[0] * n, p1[1] * n, p1[2] * n)


def dot(p1, p2):
    return (p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2])


def dot2(m, n, o, p):
    return dot(sub(m, n), sub(o, p))


def test_stone(pos, vel):
    for k in range(len(stones)):
        res = get_intersect(pos, vel, ps[k], vs[k])
        if res is None:
            return False
    return True


with open("input.txt") as f:
    pos_input, vel_input = list(zip(*[x.strip().split('@') for x in f.readlines()]))

    ps = [tuple(map(int, pos.split(','))) for pos in pos_input]
    vs = [tuple(map(int, vel.split(','))) for vel in vel_input]
    stones = list(zip(ps, vs))

    fitting_rock_vel = [None, None, None]

    for rock_vel in range(-1000, 1000):
        for k in range(3):
            is_valid = True
            for i in range(len(stones)):
                for j in range(len(stones)):
                    if i == j or vs[i][k] != vs[j][k] or rock_vel == vs[i][k]:
                        continue
                    pos_diff = abs(ps[j][k] - ps[i][k])
                    vel_diff = rock_vel - vs[i][k]
                    if pos_diff % vel_diff != 0:
                        is_valid = False
                        break
                if not is_valid:
                    break
            if is_valid:
                fitting_rock_vel[k] = rock_vel
                print("vel", k, ":", rock_vel)
                continue

    intersect = get_any_intersect(ps[0], sub(fitting_rock_vel, vs[0]), ps[1], sub(fitting_rock_vel, vs[1]))[0]
    print(intersect[0] + intersect[1] + intersect[2])
