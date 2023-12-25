from collections import deque, defaultdict


def bfs(start, graph: dict):
    q = deque()
    q.appendleft(start)
    v = {}
    v[start] = 0
    while len(q) > 0:
        cur = q.pop()
        for nei in graph[cur]:
            if nei not in v:
                v[nei] = v[cur] + 1
                q.appendleft(nei)

    return v


def shortest_path(start, end, graph: dict):
    q = deque()
    q.appendleft((start, []))
    v = set()
    v.add(start)
    while len(q) > 0:
        cur, path = q.pop()
        for nei in graph[cur]:
            if nei == end:
                return path + [(cur, nei)]
            if nei not in v:
                v.add(nei)
                q.appendleft((nei, path + [(cur, nei)]))

    return None


def try_find_cut(graph: dict[str, list], start, end, removed_edges):
    path = shortest_path(start, end, graph)

    if path == None:
        return removed_edges

    if len(removed_edges) == 3:
        return None

    for edge in path:
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
        removed_edges.append(edge)
        res = try_find_cut(graph, start, end, removed_edges)

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

        if res is not None:
            return res

        removed_edges.remove(edge)


def find_cut(graph):
    for start in graph:
        dists = bfs(start, graph)
        max_dist = max(dists.values())
        end = [x for x in dists if dists[x] == max_dist][0]

        res = try_find_cut(graph, start, end, [])
        if res is not None:
            return res


def is_bisected(graph: dict):
    first_item = list(graph.keys())[0]
    q = deque()
    q.appendleft(first_item)
    v = set()
    v.add(first_item)
    while len(q) > 0:
        cur = q.pop()
        for nei in graph[cur]:
            if nei not in v:
                v.add(nei)
                q.appendleft(nei)
    val = len(v) * (len(graph) - len(v))
    return val if len(v) != len(graph) else None


with open("input.txt") as f:
    lines = [(y[0], y[1].strip().split(' ')) for y in [x.strip().split(':') for x in f.readlines()]]

    graph = defaultdict(set)
    for node, neighbours in lines:
        for n in neighbours:
            graph[node].add(n)
            graph[n].add(node)

    graph = {x: list(graph[x]) for x in graph}
    cut = find_cut(graph)

    for edge in cut:
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])

    print(is_bisected(graph))
