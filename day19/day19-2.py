from collections import deque


def do_split(val_range, value, comp_type):
    min_v, max_v = val_range
    if comp_type == '<':
        if max_v < value:
            return [(min_v, max_v)], []
        if min_v >= value:
            return [], [(min_v, max_v)]
        return [(min_v, value - 1)], [(value, max_v)]
    if comp_type == '>':
        if min_v > value:
            return [(min_v, max_v)], []
        if max_v <= value:
            return [], [(min_v, max_v)]
        return [(value + 1, max_v)], [(min_v, value)]


def do_comp(part: dict, rule_name, rules):
    print(part, rule_name)
    if rule_name == 'A':
        return [(part, 'A')]
    if rule_name == 'R':
        return [(part, 'R')]

    sections, default_destination = rules[rule_name]

    results = []
    for (param, comp_type, value, destination) in sections:
        val_ranges = part[param]
        split_ranges = []
        passing_ranges = []
        for r in val_ranges:
            split_r = do_split(r, value, comp_type)
            split_ranges.extend(split_r[0])
            passing_ranges.extend(split_r[1])

        accepted_part = part.copy()
        accepted_part[param] = split_ranges
        part[param] = passing_ranges

        results.extend(do_comp(accepted_part, destination, rules))

    results.extend(do_comp(part, default_destination, rules))
    return results


with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    empty_line = lines.index('')
    rules = lines[:empty_line]

    parsed_rules = {}
    for rule in rules:
        first_bracket = rule.index('{')
        name = rule[:first_bracket]
        sections = rule[first_bracket+1:-1].split(',')
        parsed_sections = []
        default_destination = sections[-1]
        for section in sections[:-1]:
            comp_type = '<' if '<' in section else '>'
            comp_i = section.index(comp_type)
            colon_i = section.index(':')
            parameter = section[:comp_i]
            value = int(section[comp_i+1:colon_i])
            destination = section[colon_i+1:]
            parsed_sections.append((parameter, comp_type, value, destination))
        print(name, parsed_sections, default_destination)

        parsed_rules[name] = (parsed_sections, default_destination)

    print(parsed_rules)

    start_range = {'x': [(1, 4000)], 's': [(1, 4000)], 'm': [(1, 4000)], 'a': [(1, 4000)]}
    result = do_comp(start_range, 'in', parsed_rules)
    sums = 0
    for r in result:
        if r[1] == 'A':
            possibs = (r[0]['a'][0][1] - r[0]['a'][0][0] + 1) * (r[0]['x'][0][1] - r[0]['x'][0][0] + 1) * (r[0]['s'][0][1] - r[0]['s'][0][0] + 1) * (r[0]['m'][0][1] - r[0]['m'][0][0] + 1)
            sums += possibs
            print(possibs)
        print(r)
    print(sums)
