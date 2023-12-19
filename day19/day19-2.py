def do_split(val_range, value, comp_type):
    min_v, max_v = val_range
    if comp_type == '<':
        if max_v < value:
            return (min_v, max_v), None
        if min_v >= value:
            return None, (min_v, max_v)
        return (min_v, value - 1), (value, max_v)
    if comp_type == '>':
        if min_v > value:
            return (min_v, max_v), None
        if max_v <= value:
            return None, (min_v, max_v)
        return (value + 1, max_v), (min_v, value)


def do_comp(part: dict, rule_name, rules):
    print(part, rule_name)
    if rule_name == 'A':
        return [part]
    if rule_name == 'R':
        return []

    sections, default_destination = rules[rule_name]

    results = []
    for (param, comp_type, value, destination) in sections:
        val_range = part[param]
        accepted_range, passing_range = do_split(val_range, value, comp_type)

        if accepted_range is not None:
            accepted_part = part.copy()
            accepted_part[param] = accepted_range

            results.extend(do_comp(accepted_part, destination, rules))
        part[param] = passing_range
        if passing_range is None:
            return results

    results.extend(do_comp(part, default_destination, rules))
    return results


with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    rules = lines[:lines.index('')]

    parsed_rules = {}
    for rule in rules:
        first_bracket = rule.index('{')
        name = rule[:first_bracket]
        sections = rule[first_bracket+1:-1].split(',')
        parsed_sections = []
        default_destination = sections[-1]
        for section in sections[:-1]:
            comp_type = '<' if '<' in section else '>'
            comp_i, colon_i = section.index(comp_type), section.index(':')
            parsed_sections.append((section[:comp_i], comp_type, int(section[comp_i+1:colon_i]), section[colon_i+1:]))

        parsed_rules[name] = (parsed_sections, default_destination)

    start_range = {'x': (1, 4000), 's': (1, 4000), 'm': (1, 4000), 'a': (1, 4000)}
    results = do_comp(start_range, 'in', parsed_rules)
    sums = sum([(r['a'][1] - r['a'][0] + 1) * (r['x'][1] - r['x'][0] + 1) * (r['s'][1] - r['s'][0] + 1) * (r['m'][1] - r['m'][0] + 1) for r in results])
    print(sums)
