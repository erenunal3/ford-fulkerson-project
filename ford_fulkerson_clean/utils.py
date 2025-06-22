import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def draw_graph(graph, title="Graph"):
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, capacity=graph[u][v])

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'capacity')

    plt.figure(figsize=(8, 6))
    plt.title(title)  # Başlık ekleniyor
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    st.pyplot(plt)
    plt.clf()

