def win_num(card):
    winning, current = card
    wins = [val for val in current if val in winning]
    return len(wins)

with open('day4.txt') as f:
    lines = [[[z for z in y.split(' ') if z != ''] for y in x.strip().split(':')[1].split('|')] for x in f.readlines()]

    counts = [1 for _ in lines]
    for (i, card) in enumerate(lines):
        wins = win_num(card)
        print(wins)
        for wi in range(1, wins + 1):
            counts[i + wi] += counts[i]
        print(counts)

    print(counts)
    print(lines)
    print(sum(counts))
