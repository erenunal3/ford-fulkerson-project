def bfs(graph, source, sink, parent):
    visited = set()
    queue = [source]
    visited.add(source)

    while queue:
        u = queue.pop(0)
        for v in graph.get(u, {}):
            if v not in visited and graph[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    residual = {u: dict(graph[u]) for u in graph}
    max_flow = 0
    parent = {}

    while bfs(residual, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual.setdefault(v, {}).setdefault(u, 0)
            residual[v][u] += path_flow
            v = u
        parent = {}
    return max_flow
