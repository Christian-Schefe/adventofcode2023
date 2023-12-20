from collections import deque


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
    print(destinations)
    print(modules)
    print(mod_by_name)
    print(flip_flop_states)
    print(conjunction_sources)

    low_count = 0
    high_count = 0

    for i in range(1000):
        q = deque()
        q.appendleft((False, 'broadcaster', None))

        while len(q) > 0:
            (signal, target, origin) = q.pop()
            if signal:
                high_count += 1
            else:
                low_count += 1

            # print(origin, '-high' if signal else '-low', "->", target)

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

    print(low_count, high_count)
    print(low_count * high_count)