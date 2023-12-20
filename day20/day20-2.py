from collections import deque
from math import lcm

with open("input.txt") as f:
    lines = [[y.strip() for y in x.strip().split('->')] for x in f.readlines()]
    destinations = [[y.strip() for y in x[1].split(',')] for x in lines]
    modules = [(x[0][0], x[0][1:]) if x[0] != 'broadcaster' else ('b', x[0]) for x in lines]
    mod_by_name = {name: (mod_type, dest) for dest, (mod_type, name) in zip(destinations, modules)}
    conjuction_mods = [name for name, (mod_type, _) in mod_by_name.items() if mod_type == '&']
    conjunction_sources = {name: {} for name in conjuction_mods}
    for mod, (mod_type, dest) in mod_by_name.items():
        for d in dest:
            if d in conjunction_sources:
                conjunction_sources[d][mod] = False

    flip_flop_states = {name: False for name, (mod_type, _) in mod_by_name.items() if mod_type == '%'}
    first_high_mfs = {}

    # ONLY WORKS IF EXACTLY ONE MODULE OUTPUTS TO 'rx' (and that module should be a conjunction module)
    BEFORE_OUTPUT_MODULE = 'mf'

    i = 0
    while True:
        i += 1
        q = deque()
        q.appendleft((False, 'broadcaster', None))

        if len(first_high_mfs) == len(conjunction_sources[BEFORE_OUTPUT_MODULE]):
            break

        while len(q) > 0:
            (signal, target, origin) = q.pop()

            if target == BEFORE_OUTPUT_MODULE and signal:
                if origin not in first_high_mfs:
                    first_high_mfs[origin] = i

            if target not in mod_by_name:
                continue

            (mod_type, dests) = mod_by_name[target]

            if mod_type == 'b':
                output_signal = signal
            elif mod_type == '%':
                if signal:
                    continue
                output_signal = not flip_flop_states[target]
                flip_flop_states[target] = output_signal
            elif mod_type == '&':
                conjunction_sources[target][origin] = signal
                output_signal = False in conjunction_sources[target].values()

            for dest in dests:
                q.appendleft((output_signal, dest, target))

    print(first_high_mfs)
    mult_val = 1
    for v in first_high_mfs.values():
        mult_val *= v
    print(mult_val)
    print(lcm(*first_high_mfs.values()))
