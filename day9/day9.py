

def extrapolate(se):
    rows = [se]
    has_nonzero = True
    while has_nonzero:
        has_nonzero = False
        new_row = []
        for i in range(1, len(rows[-1])):
            diff = rows[-1][i] - rows[-1][i - 1]
            new_row.append(diff)
            if diff != 0:
                has_nonzero = True
        rows.append(new_row)
        if not has_nonzero:
            break

    print(rows)

    rows[-1].append(0)

    for i in range(len(rows) - 2, -1, -1):
        new_val = rows[i][-1] + rows[i + 1][-1]
        rows[i].append(new_val)
    print(rows)
    return rows[0][-1]

def extrapolate2(se):
    rows = [se]
    has_nonzero = True
    while has_nonzero:
        has_nonzero = False
        new_row = []
        for i in range(1, len(rows[-1])):
            diff = rows[-1][i] - rows[-1][i - 1]
            new_row.append(diff)
            if diff != 0:
                has_nonzero = True
        rows.append(new_row)
        if not has_nonzero:
            break

    print(rows)

    rows = [list(reversed(row)) for row in rows]

    rows[-1].append(0)

    for i in range(len(rows) - 2, -1, -1):
        new_val = rows[i][-1] - rows[i + 1][-1]
        rows[i].append(new_val)
    print(rows)
    return rows[0][-1]



with open("day9.txt") as f:
    sequences = [list(map(int, l.strip().split(' '))) for l in f.readlines()]
    print(sum(map(extrapolate2, sequences)))