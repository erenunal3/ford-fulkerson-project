import streamlit as st

def ford_fulkerson(g, s, t):
    def bfs(r, s, t, p):
        v = set()
        q = [s]
        v.add(s)
        while q:
            u = q.pop(0)
            for n in r.get(u, {}):
                if n not in v and r[u][n] > 0:
                    q.append(n)
                    v.add(n)
                    p[n] = u
                    if n == t:
                        return True
        return False

    r = {u: dict(g[u]) for u in g}
    mf = 0
    p = {}
    while bfs(r, s, t, p):
        pf = float('inf')
        n = t
        while n != s:
            pf = min(pf, r[p[n]][n])
            n = p[n]
        mf += pf
        n = t
        while n != s:
            u = p[n]
            r[u][n] -= pf
            r.setdefault(n, {}).setdefault(u, 0)
            r[n][u] += pf
            n = u
        p = {}
    return mf

# Basit arayüz
st.title("Maksimum Akış Hesaplama (Basit)")

if st.button("Çalıştır"):
    graph = {
        'S': {'A': 16, 'C': 13},
        'A': {'B': 12},
        'B': {'T': 20},
        'C': {'A': 4, 'D': 14},
        'D': {'B': 7, 'T': 4},
        'T': {}
    }

    result = ford_fulkerson(graph, 'S', 'T')
    st.write(f"Maksimum Akış: {result}")