from collections import Counter


def strength(hand: str):
    lexi = hand.replace('T', 'B').replace('J', '0').replace('Q', 'D').replace('K', 'E').replace('A', 'F')
    s = Counter(list(hand))
    max_c = max(s.values())
    if len(s) == 1:
        return (7, lexi)
    if len(s) == 2:
        if 'J' in s and s['J'] > 0:
            return (7, lexi)
        elif max_c == 4:
            return (6, lexi)
        else:
            return (5, lexi)
    if len(s) == 3:
        if max_c == 3:
            if 'J' in s:
                return (6, lexi)
            return (4, lexi)
        else:
            if 'J' in s and s['J'] == 2:
                return (6, lexi)
            if 'J' in s:
                return (5, lexi)
            return (3, lexi)
    if len(s) == 4:
        if 'J' in s:
            return (4, lexi)
        return (2, lexi)
    else:
        if 'J' in s:
            return (2, lexi)
        return (1, lexi)


with open("day6.txt") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    stre = [strength(y[0]) for y in lines]
    sort = list(sorted(zip(stre, lines)))
    s = 0
    for (r, l) in enumerate(sort):
        print(r+1, l)
        s += (r + 1) * int(l[1][1])
    print(s)
