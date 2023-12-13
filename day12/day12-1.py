def brute_force(problem, grouping):
    possibilities = [problem[0]] if problem[0] != "?" else [".", "#"]
    for j in range(1, len(problem)):
        new_possibilities = []
        for possib in possibilities:
            if problem[j] != "?":
                new_possibilities.append(possib + problem[j])
            else:
                new_possibilities.append(possib + ".")
                new_possibilities.append(possib + "#")

        possibilities = new_possibilities

    sections = [([len(y) for y in p.split('.') if y != ''], p) for p in possibilities]
    count = [section for section in sections if section[0] == grouping]
    return len(count)


with open("input.txt") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    groups = [list(map(int, x[1].split(","))) for x in lines]
    problems = [x[0] for x in lines]

    val_sum = 0
    for i in range(len(problems)):
        val_sum += brute_force(problems[i], groups[i])
    print(val_sum)
