from unittest import TestCase
from exercises.knight_probability import MOVES, MOVE_PROBABILITY
from exercises.knight_probability.src import knight_probability


class KnightProbabilityTest(TestCase):

    def test_out_of_bounds_initialization(self):

        cases = (
            {"m": 1, "n": 1, "x": 1, "y": 1},
            {"m": 2, "n": 1, "x": 1, "y": 1},
            {"m": 1, "n": 2, "x": 1, "y": 1},
            {"m": 2, "n": 3, "x": 2, "y": 1},
            {"m": 2, "n": 3, "x": 1, "y": 3},
        )

        for case in cases:
            with self.subTest(case):
                expected = {
                    (case["x"], case["y"]): 0
                }
                r = knight_probability(
                        m=case["m"],
                        n=case["n"],
                        x=case["x"],
                        y=case["y"],
                        k=0
                    )

                self.assertEqual(r, expected)

    def test_initialization_trivial_case(self):

        cases = (
            {"m": 1, "n": 1, "x": 0, "y": 0},
            {"m": 2, "n": 1, "x": 1, "y": 0},
            {"m": 1, "n": 2, "x": 0, "y": 1},
            {"m": 2, "n": 3, "x": 0, "y": 0},
            {"m": 2, "n": 3, "x": 0, "y": 1},
            {"m": 2, "n": 3, "x": 0, "y": 2},
            {"m": 2, "n": 3, "x": 1, "y": 0},
            {"m": 2, "n": 3, "x": 1, "y": 1},
            {"m": 2, "n": 3, "x": 1, "y": 2},
        )

        for case in cases:
            with self.subTest(case):
                expected = {
                    (case["x"], case["y"]): 1
                }
                r = knight_probability(
                        m=case["m"],
                        n=case["n"],
                        x=case["x"],
                        y=case["y"],
                        k=0
                    )

                self.assertEqual(r, expected)

    def test_first_time_step(self):

        expected = {
            (2 + m[0], 2 + m[1]): MOVE_PROBABILITY
            for m in MOVES
        }
        r = knight_probability(
            m=5,
            n=5,
            x=2,
            y=2,
            k=2
        )

        self.assertEqual(sum(r.values()), 1)
        self.assertEqual(r, expected)
