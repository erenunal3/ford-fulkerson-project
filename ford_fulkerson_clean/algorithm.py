def ford_fulkerson(graph, source, sink):
    residual_graph = {u: dict(v) for u, v in graph.items()}
    max_flow = 0
    steps = []

    while True:
        visited = set()
        parent = {}

        def dfs(u):
            visited.add(u)
            if u == sink:
                return True
            for v in residual_graph.get(u, {}):
                if v not in visited and residual_graph[u][v] > 0:
                    parent[v] = u
                    if dfs(v):
                        return True
            return False

        found_path = dfs(source)
        if not found_path:
            break

        path = []
        v = sink
        path_flow = float('inf')
        while v != source:
            u = parent[v]
            path.insert(0, (u, v))
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph.setdefault(v, {})
            residual_graph[v][u] = residual_graph[v].get(u, 0) + path_flow
            v = u

        max_flow += path_flow
        steps.append({
            'path': path,
            'path_flow': path_flow,
            'residual_graph': {u: dict(v) for u, v in residual_graph.items()}
        })

    return max_flow, steps

