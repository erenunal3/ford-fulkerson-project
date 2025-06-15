import streamlit as st
from algorithm import ford_fulkerson
from utils import draw_graph

# Default graph data
default_graph = {
    'S': {'A': 16, 'C': 13},
    'A': {'B': 12},
    'B': {'T': 20},
    'C': {'A': 4, 'D': 14},
    'D': {'B': 7, 'T': 4},
    'T': {}
}

st.title("Ford-Fulkerson Maximum Flow Visualizer")

st.sidebar.header("Graph Input")

use_default = st.sidebar.checkbox("Use default graph", value=True)

if use_default:
    graph = default_graph
else:
    st.warning("Currently, only the default graph is supported.")
    graph = default_graph

source = st.sidebar.text_input("Source node", "S")
sink = st.sidebar.text_input("Sink node", "T")

if st.button("Run Algorithm"):
    st.subheader("1. Initial Graph")
    draw_graph(graph, title="Initial Graph")

    max_flow, steps = ford_fulkerson(graph, source, sink)

    for i, step in enumerate(steps):
        st.subheader(f"Step {i+1}: Flow = {step['path_flow']}")
        draw_graph(step['residual_graph'], title=f"Residual Graph (Step {i+1})", path=step['path'])

    st.success(f"🔚 Maximum Flow: {max_flow}")
