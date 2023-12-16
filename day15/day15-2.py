def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


with open("input.txt") as f:
    strings = f.read().strip().split(',')
    labels = [(x.split('=') if '=' in x else x.split('-'))[0] for x in strings]

    last_strengths = {}

    hashes = list(map(hash, labels))
    boxes = [[] for _ in range(256)]

    for i in range(len(strings)):
        box = hashes[i]
        lbl = labels[i]
        if '-' in strings[i] and lbl in last_strengths:
            strength = last_strengths[lbl]
            if (lbl, strength) in boxes[box]:
                boxes[box].remove((lbl, strength))
        elif '=' in strings[i]:
            if lbl in last_strengths and (lbl, last_strengths[lbl]) in boxes[box]:
                j = boxes[box].index((lbl, last_strengths[lbl]))
                strength = strings[i].split('=')[1]
                boxes[box][j] = (lbl, strength)
                last_strengths[lbl] = strength
            else:
                strength = strings[i].split('=')[1]
                boxes[box].append((lbl, strength))
                last_strengths[lbl] = strength

    vals = 0
    for i, box in enumerate(boxes):
        for j, item in enumerate(box):
            vals += (i + 1) * (j + 1) * int(item[1])
    print(labels, hashes, boxes)
    print(vals)
