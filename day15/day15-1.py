def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

with open("input.txt") as f:
    strings = f.read().strip().split(',')
    print(strings)
    print(sum(map(hash, strings)))