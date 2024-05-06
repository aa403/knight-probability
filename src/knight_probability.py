from collections import defaultdict

MOVES = (
    (2, 1),
    (1, 2),
    (-2, 1),
    (-1, 2),
    (2, -1),
    (1, -2),
    (-2, -1),
    (-1, -2),
)

MOVE_PROBABILITY = round(1 / 8, 4)


def rounded_float(f: float):
    return round(f, 8)


def knight_probability(m: int, n: int, x: int, y: int, k: int) -> dict:
    """

    Args:
        m: number of columns on the board
        n: number of rows on the board
        x: starting column position [zero based]
        y: starting row position [zero based]
        k: number of moves to consider

    Returns:

    """

    if (x < 0) or (y < 0):
        return {(x, y): 0}

    elif (x >= m) or (y >= n):
        return {(x, y): 0}

    else:
        p = {(x, y): 1}

    t = 0

    while t < k:
        # store results from this loop
        new_p = defaultdict(float)

        # iterate over each key
        for start_point in p:

            # get the probability that we're at that start point
            starting_probability = p[start_point]
            target_probability = rounded_float(starting_probability * MOVE_PROBABILITY)

            for move in MOVES:
                new_x = start_point[0] + move[0]
                if (new_x >= m) or (new_x < 0):
                    continue

                new_y = start_point[1] + move[1]
                if (new_y >= n) or (new_y < 0):
                    continue

                new_p[(new_x, new_y)] += target_probability

            pass

        p = new_p
        t += 1

    return p
