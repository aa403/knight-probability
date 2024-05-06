# About

This is an implementation of the knight probablity challenge as described here: https://leetcode.com/problems/knight-probability-in-chessboard/description/

Rather than consider a square board as in the exercise, the row and column dimensions can be variable. 

The solution is also wrapped in a streamlit application which allows for visualisation of the resulting board.

We result in an algorithm of `O(mnk)` where `m, n` are columns and rows; and k is the number of timesteps considered.


# Usage

bring this up in a container using:
```shell
path/to/project/ $ docker compose up -d
```

access from `localhost:8501`


# Development:

using python 3.11

create a virtual environment

activate the virtual environment and install dependencies 

```shell
path/to/project/ $ poetry install --no-dev
```

OR 

```shell
path/to/project/ $ pip install -r requirements.txt
```

run the application:

```shell
path/to/project/ $ streamlit run src/streamlit_app.py
```