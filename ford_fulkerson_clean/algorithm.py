from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in residual_graph[u]:
            if v not in visited and residual_graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

def ford_fulkerson(graph, source, sink):
    residual_graph = {u: dict(v) for u, v in graph.items()}
    max_flow = 0
    steps = []

    parent = {}

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        path = []

        while s != source:
            path.insert(0, s)
            u = parent[s]
            path_flow = min(path_flow, residual_graph[u][s])
            s = u
        path.insert(0, source)

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow
        step_copy = {u: dict(v) for u, v in residual_graph.items()}
        steps.append({'residual_graph': step_copy, 'path': path, 'path_flow': path_flow})

    return max_flow, steps


