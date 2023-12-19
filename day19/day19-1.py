from collections import deque


def do_comp(part, rule_name, rules):
    print(part, rule_name)
    if rule_name == 'A':
        return 'A'
    if rule_name == 'R':
        return 'R'

    sections, default_destination = rules[rule_name]
    for (param, comp_type, value, destination) in sections:
        val = part[param]
        accepted = val < value if comp_type == '<' else val > value
        if accepted:
            return do_comp(part, destination, rules)

    return do_comp(part, default_destination, rules)


with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    empty_line = lines.index('')
    rules = lines[:empty_line]
    parts = [[x.split('=') for x in p[1:-1].split(',')] for p in lines[empty_line+1:]]
    parts = [{p[0]: int(p[1]) for p in x} for x in parts]

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
    print(parts)

    sums = 0

    for part in parts:
        dest = do_comp(part, 'in', parsed_rules)
        if dest == 'A':
            sums += sum(part.values())

    print(sums)
