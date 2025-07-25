import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def draw_graph(graph, title="", path=None):
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, capacity=graph[u][v])

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'capacity')

    plt.figure(figsize=(8, 6))
    edge_colors = ['red' if path and (u in path and v in path and path.index(v) - path.index(u) == 1) else 'black' for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrows=True, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    st.pyplot(plt)
    plt.clf()


