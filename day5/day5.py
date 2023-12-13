def get_num(map, num):
    for row in map:
        if row[1] > num:
            continue
        if row[1] + row[2] <= num:
            continue
        return row[0] + (num - row[1])
    return num


def subdiv_range(seed_range, map):
    in_min = map[1]
    out_min = map[0]

    in_max = map[1] + map[2]
    out_max = map[0] + map[2]

    map_dif = map[3]

    if seed_range[0] >= in_max:
        return [seed_range], []
    if seed_range[1] <= in_min:
        return [seed_range], []

    if seed_range[1] >= in_max:
        if seed_range[0] < in_min:
            return [(seed_range[0], in_min), (in_max, seed_range[1])], [(out_min, out_max)]
        else:
            return [(in_max, seed_range[1])], [(seed_range[0] + map_dif, out_max)]
    else:
        if seed_range[0] < in_min:
            return [(seed_range[0], in_min)], [(out_min, seed_range[1] + map_dif)]
        else:
            return [], [(seed_range[0] + map_dif, seed_range[1] + map_dif)]


def subdiv_ranges(seed_ranges, maps):
    cur_ranges = seed_ranges
    out_ranges = []
    for map in maps:
        new_ranges = []
        for range in cur_ranges:
            unmapped_p, mapped_p = subdiv_range(range, map)
            new_ranges += unmapped_p
            out_ranges += mapped_p
        cur_ranges = new_ranges
    
    out_ranges += cur_ranges
    return out_ranges



with open("day5.txt") as f:
    lines = [x.strip() for x in f.readlines() if "-" not in x]
    seeds = [int(num) for num in lines.pop(0).split(":")[1].strip().split(" ")]
    seed_ranges = []
    for i in range(len(seeds)):
        print(i)
        if (i % 2) != 0:
            continue
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    print(seed_ranges)

    maps = []
    cur_map = []
    for line in lines[1:]:
        if line == "":
            maps.append(cur_map)
            cur_map = []
        else:
            mp = [int(num) for num in line.split(" ")]
            cur_map.append(mp + [mp[0] - mp[1]])

    if len(cur_map) > 0:
        maps.append(cur_map)

    print(maps)

    mapped_ranges = subdiv_ranges(seed_ranges[:1], maps[0])
    mapped_ranges2 = subdiv_ranges(mapped_ranges, maps[1])
    mapped_ranges3 = subdiv_ranges(mapped_ranges2, maps[2])
    mapped_ranges4 = subdiv_ranges(mapped_ranges3, maps[3])
    mapped_ranges5 = subdiv_ranges(mapped_ranges4, maps[4])
    mapped_ranges6 = subdiv_ranges(mapped_ranges5, maps[5])
    mapped_ranges7 = subdiv_ranges(mapped_ranges6, maps[6])
    print("s-s", mapped_ranges)
    print("   ", mapped_ranges2)
    print("f-w", mapped_ranges3)
    print("   ", mapped_ranges4)
    print("l-t", mapped_ranges5)
    print("   ", mapped_ranges6)
    print("h-l", mapped_ranges7)

    print(min([x[0] for x in mapped_ranges7]))
