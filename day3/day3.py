with open("day3.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    star_pos = [[0 for _ in line] for line in lines]
    adjacencies = {}

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == '*':
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= (y + dy) < len(lines) and 0 <= (x + dx) < len(line):
                            print((x + dx), (y + dy))
                            star_pos[y + dy][x+dx] = (x, y)
                            adjacencies[(x, y)] = []

    print(star_pos)

    numbers = []
    for y in range(len(lines)):
        line = lines[y]
        cur_num = None
        num_start = 0
        for x in range(len(line)):
            if line[x] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if cur_num == None:
                    cur_num = int(line[x])
                    num_start = x
                else:
                    cur_num = 10 * cur_num + int(line[x])
            elif cur_num != None:
                for dx in range(x - num_start):
                    sp = star_pos[y][num_start + dx]
                    if sp != 0:
                        adjacencies[sp].append(cur_num)
                        break
                cur_num = None
        if cur_num != None:
            for dx in range(x - num_start):
                sp = star_pos[y][num_start + dx]
                if sp != 0:
                    adjacencies[sp].append(cur_num)
                    break
            cur_num = None


    print(adjacencies)
    gear_ratios = [val[0] * val[1] for val in adjacencies.values() if (val != 0) and len(val) == 2]

    print(gear_ratios)
    print(sum(gear_ratios))

    # lines = [list(line.strip()) for line in f.readlines()]
    # symbol_pos = [[0 for _ in line] for line in lines]
    # for y in range(len(lines)):
    #     line = lines[y]
    #     for x in range(len(line)):
    #         if line[x] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    #             for dy in range(-1, 2):
    #                 for dx in range(-1, 2):
    #                     if 0 <= (y + dy) < len(lines) and 0 <= (x + dx) < len(line):
    #                         print((x + dx), (y + dy))
    #                         symbol_pos[y + dy][x+dx] = 1

    # numbers = []
    # sum = 0
    # for y in range(len(lines)):
    #     line = lines[y]
    #     cur_num = None
    #     num_start = 0
    #     for x in range(len(line)):
    #         if line[x] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    #             if cur_num == None:
    #                 cur_num = int(line[x])
    #                 num_start = x
    #             else:
    #                 cur_num = 10 * cur_num + int(line[x])
    #         elif cur_num != None:
    #             for dx in range(x - num_start):
    #                 if symbol_pos[y][num_start + dx] == 1:
    #                     numbers.append(cur_num)
    #                     sum += cur_num
    #                     break
    #             cur_num = None
    #     if cur_num != None:
    #         for dx in range(x - num_start):
    #             if symbol_pos[y][num_start + dx] == 1:
    #                 numbers.append(cur_num)
    #                 sum += cur_num
    #                 break
#             cur_num = None


    # # print(symbol_pos)
    # # print(numbers)
    # print(sum)
