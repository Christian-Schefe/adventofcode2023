def get_intersect(pos_a, vel_a, pos_b, vel_b):
    p1, p2, p3, p4 = pos_a, add(pos_a, vel_a), pos_b, add(pos_b, vel_b)

    divisor = (dot2(p2, p1, p2, p1) * dot2(p4, p3, p4, p3) - dot2(p4, p3, p2, p1) * dot2(p4, p3, p2, p1))
    if divisor == 0:
        return None,
    mua = (dot2(p1, p3, p4, p3) * dot2(p4, p3, p2, p1) - dot2(p1, p3, p2, p1) * dot2(p4, p3, p4, p3)) / divisor
    mub = (dot2(p1, p3, p4, p3) + mua * dot2(p4, p3, p2, p1)) / dot2(p4, p3, p4, p3)

    return add(pos_a, mul(vel_a, int(mua)))


def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])


def sub(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def mul(p1, n):
    return (p1[0] * n, p1[1] * n, p1[2] * n)


def dot(p1, p2):
    return (p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2])


def dot2(m, n, o, p):
    return dot(sub(m, n), sub(o, p))


with open("input.txt") as f:
    pos_input, vel_input = list(zip(*[x.strip().split('@') for x in f.readlines()]))

    ps = [tuple(map(int, pos.split(','))) for pos in pos_input]
    vs = [tuple(map(int, vel.split(','))) for vel in vel_input]

    fitting_rock_vel = [None, None, None]

    for k in range(3):
        for rock_vel in range(-500, 500):
            is_valid = True
            for i in range(len(ps)):
                for j in range(len(ps)):
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
                print("vel", ['x', 'y', 'z'][k], ":", rock_vel)
                break

    intersect = get_intersect(ps[0], sub(fitting_rock_vel, vs[0]), ps[1], sub(fitting_rock_vel, vs[1]))
    print(intersect[0] + intersect[1] + intersect[2])
