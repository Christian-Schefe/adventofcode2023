def is_possible(game):
    for set in game:
        for (num, type) in set:
            n = int(num)
            if type == "blue" and n > 14:
                return False
            if type == "green" and n > 13:
                return False
            if type == "red" and n > 12:
                return False
    return True

def get_min(game):
    min_b = 0
    min_g = 0
    min_r = 0
    for set in game:
        for (num, type) in set:
            n = int(num)
            if type == "blue" and n > min_b:
                min_b = n
            if type == "green" and n > min_g:
                min_g = n
            if type == "red" and n > min_r:
                min_r = n

    return min_b * min_g * min_r

with open("day2.txt") as f:
    lines = [line.strip().split(':')[1].strip() for line in f.readlines()]
    games = [line.split(';') for line in lines]
    sets = [[s.strip().split(',') for s in game] for game in games]
    blocks = [[[a.strip().split(' ') for a in s] for s in game] for game in sets]
    print(blocks)

    sum = 0

    for i in range(len(blocks)):
        sum += get_min(blocks[i])

    print(sum)

