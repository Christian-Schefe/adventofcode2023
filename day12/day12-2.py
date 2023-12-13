def matches(pattern, problem):
    for a, b in zip(pattern, problem):
        if b != "?" and a != b:
            return False
    return True


def solve_problem(problem, grouping, dots, cache, prefix=""):
    key = (dots, tuple(grouping))
    if key in cache:
        return cache[key]

    if len(grouping) == 0:
        res_val = 1 if matches(prefix + '.' * dots, problem) else 0
        cache[key] = res_val
        return res_val

    positions = []
    for dots_to_place in range(1 if prefix != "" else 0, dots + 1):
        pattern = prefix + "." * dots_to_place + "#" * grouping[0]
        if matches(pattern, problem):
            positions.append((dots_to_place, pattern))

    sums = 0
    for (dp, prefix) in positions:
        sums += solve_problem(problem, grouping[1:], dots - dp, cache, prefix)

    cache[key] = sums
    return sums


with open("input.txt") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    groups = [list(map(int, x[1].split(","))) * 5 for x in lines]
    problems = ["?".join([x[0] for _ in range(5)]) for x in lines]

    val_sum = 0
    for i in range(len(lines)):
        cache = {}
        dots = len(problems[i]) - sum(groups[i])
        val_sum += solve_problem(problems[i], groups[i], dots, cache)
    print(val_sum)
