from collections import deque, defaultdict


def drop_block(block, block_i, grid):
    important_xy = [(x, y) for x in range(block[0][0], block[1][0] + 1) for y in range(block[0][1], block[1][1] + 1)]
    cur_z = block[0][2]
    z_diff = block[1][2] - block[0][2]
    while True:
        if cur_z == 1:
            break
        cur_z -= 1
        failure = False
        for x, y in important_xy:
            coord = (x, y, cur_z)
            if coord in grid and grid[coord] != block_i:
                failure = True
                cur_z += 1
                break
        if failure:
            break

    block = ([block[0][0], block[0][1], cur_z], [block[1][0], block[1][1], cur_z + z_diff])
    return block


def get_supporters_and_supported(block, block_i, grid):
    important_xy = [(x, y) for x in range(block[0][0], block[1][0] + 1) for y in range(block[0][1], block[1][1] + 1)]
    supporters = set()
    supported = set()
    for x, y in important_xy:
        bottom_coord = (x, y, block[0][2] - 1)
        top_coord = (x, y, block[1][2] + 1)
        if bottom_coord in grid:
            supporters.add(grid[bottom_coord])
        if top_coord in grid:
            supported.add(grid[top_coord])

    return supporters, supported


def get_fall_count(block_i, supps: list[tuple[set, set]], coords):
    cache = {block_i: True}
    return len([1 for i, _ in enumerate(coords) if will_fall(i, supps, cache) and i != block_i])


def will_fall(block_i, supps, cache: dict):
    if block_i in cache:
        return cache[block_i]
    supporters = supps[block_i][0]
    for i in supporters:
        wf = will_fall(i, supps, cache)
        if not wf:
            cache[block_i] = False
            return False
    res = len(supporters) > 0
    cache[block_i] = res
    return res


with open("input.txt") as f:
    lines = [x.strip().split('~') for x in f.readlines()]
    coords = list(zip([list(map(int, x[0].split(','))) for x in lines], [list(map(int, x[1].split(','))) for x in lines]))

    max_height = max([coord[0][2] for coord in coords])

    for i in range(max_height + 1):
        by_height = defaultdict(list)
        for j, block in enumerate(coords):
            by_height[block[0][2]].append(j)
        grid = {(x, y, z): k for k, block in enumerate(coords) for x in range(block[0][0], block[1][0] + 1) for y in range(block[0][1], block[1][1] + 1) for z in range(block[0][2], block[1][2] + 1)}

        for block_i in by_height[i]:
            new_block = drop_block(coords[block_i], block_i, grid)
            coords[block_i] = new_block

    grid = {(x, y, z): k for k, block in enumerate(coords) for x in range(block[0][0], block[1][0] + 1) for y in range(block[0][1], block[1][1] + 1) for z in range(block[0][2], block[1][2] + 1)}

    supporters_and_supported = [get_supporters_and_supported(block, block_i, grid) for block_i, block in enumerate(coords)]

    disintegration_count = 0

    for block_i, block in enumerate(coords):
        falls = get_fall_count(block_i, supporters_and_supported, coords)
        disintegration_count += falls

    print(disintegration_count)
