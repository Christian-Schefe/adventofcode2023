def solve(problem: list, height, width):
    for y in range(1, height):
        side_diff = 0
        for dy in range(1, height):
            if y - dy < 0 or y + dy - 1 >= height:
                break
            for x in range(width):
                if problem[y - dy][x] != problem[y + dy - 1][x]:
                    side_diff += 1
        if side_diff == 1:
            return 100 * y

    for x in range(1, width):
        side_diff = 0
        for dx in range(1, width):
            if x - dx < 0 or x + dx - 1 >= width:
                break
            for y in range(height):
                if problem[y][x - dx] != problem[y][x + dx - 1]:
                    side_diff += 1
        if side_diff == 1:
            return x

    print("no solution")
    return 0


with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    problems = []

    cur_problem = []
    for line in lines:
        if line == '':
            problems.append(cur_problem)
            cur_problem = []
        else:
            cur_problem.append(line)
    if len(cur_problem) > 0:
        problems.append(cur_problem)

    val_sum = 0
    for i in range(len(problems)):
        val_sum += solve(problems[i], len(problems[i]), len(problems[i][0]))
    print(val_sum)
