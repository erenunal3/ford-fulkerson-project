# Ford-Fulkerson Maximum Flow Project

This project implements the Ford-Fulkerson algorithm using Python and Streamlit. It allows users to visualize the step-by-step execution of the algorithm on a flow network and calculates the maximum flow from a source to a sink.

## Live App

https://ff-by-eren.streamlit.app/

## Features

- Ford-Fulkerson algorithm implementation
- Visual representation of each step
- Residual graph updates per step
- Final maximum flow display

## Algorithm Explanation

The Ford-Fulkerson method finds the maximum possible flow in a flow network by searching for augmenting paths using BFS and updating residual capacities.

## Time and Space Complexity

- Time: O(max_flow * E)
- Space: O(V^2)

## Project Structure

- app.py: Main Streamlit interface
- algorithm.py: Algorithm logic
- utils.py: Graph visualization helper
- requirements.txt: Project dependencies
- test_algorithm.py: Basic unit tests

## How to Run Locally

git clone https://github.com/erenunal3/ford-fulkerson-project.git
cd ford-fulkerson-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
