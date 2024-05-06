from itertools import product
import pandas as pd
import altair as alt
import streamlit as st

import knight_probability as kp


def make_chart(source: pd.DataFrame, initial: pd.DataFrame) -> alt.LayerChart:
    heatmap = alt.Chart(source).mark_rect().encode(
        alt.X('x:O', axis=alt.Axis(tickMinStep=1)),
        alt.Y('y:O', axis=alt.Axis(tickMinStep=1)),
        color='p:Q',
    ).properties(
        width=600,
        height=600
    )

    text = alt.Chart(initial).mark_point(
        color="goldenrod", size=100, filled=True
    ).encode(
        alt.X('x:O', axis=alt.Axis(tickMinStep=1)),
        alt.Y('y:O', axis=alt.Axis(tickMinStep=1)),
        tooltip=alt.value("initial position")
    ).properties(
        width=600,
        height=600
    )

    chart = heatmap + text

    return chart


def streamlit_runner():
    """
    m: number of columns on the board
    n: number of rows on the board
    x: starting column position [zero based]
    y: starting row position [zero based]
    k: number of moves to consider
    Returns:

    """

    c1, c2 = st.columns(2)

    with c1:
        st.write("### Column configuration")
        m = st.slider("number of columns on the board", min_value=1, max_value=15, value=5)
        x = st.slider("starting column position [zero based]", min_value=0, max_value=m - 1, value=2)

    with c2:
        st.write("### Row configuration")
        n = st.slider("number of rows on the board", min_value=1, max_value=15, value=5)
        y = st.slider("starting row position [zero based]", min_value=0, max_value=n - 1, value=2)

    st.write("### Time steps")
    k = st.slider("number of moves to consider", min_value=0, max_value=100, value=1)

    # get result
    r = kp.knight_probability(
        m=m,
        n=n,
        x=x,
        y=y,
        k=k
    )

    probability_on_board = kp.rounded_float(sum(r.values()))

    st.write("---")
    st.write(f"Probability of still being on the board after {k} moves: {probability_on_board}")
    st.write("---")

    # generator
    _all_possible_coordinates = product(range(m), range(n))

    # initialize a zero space for the entire board
    _source, _initial = (
        {(c[0], c[1]): 0 for c in _all_possible_coordinates},
        {(c[0], c[1]): 0 for c in _all_possible_coordinates},
    )

    # update with the coordinates we have
    _source |= r

    # also mark where the initial position was.
    # we use a separate dataframe here, just to make using Altair a bit easier for the charting step
    _initial |= {(x, y): 1}

    # drop into a dataframe so that altair can chart it
    _source = ((k[0], k[1], v) for k, v in _source.items())
    source = pd.DataFrame([{
        "x": _[0],
        "y": _[1],
        "p": _[2]
    } for _ in _source])

    _initial = ((k[0], k[1], v) for k, v in _initial.items())
    initial = pd.DataFrame([{
        "x": _[0],
        "y": _[1],
        "p": _[2]
    } for _ in _initial])

    chart = make_chart(source, initial)

    # now render the results
    c1, c2 = st.columns(2)
    c1.altair_chart(chart)
    c2.write(source)

    if st.checkbox("show data"):
        st.write({
            f"{k}": kp.rounded_float(v) for k, v in r.items()
        })


if __name__ == '__main__':
    st.set_page_config(layout="wide")
    streamlit_runner()
