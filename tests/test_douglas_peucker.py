from dp import douglas_peucker


def test_epsilon_6():
    points = [
        (1, 2),
        (-1, -1),
        (4, -1),
        (5, -2),
        (6, -2),
        (6, 1),
        (8, 2),
        (9, 4),
        (8, 6)
    ]

    result = douglas_peucker(points, 6)

    assert result == [(1, 2), (8, 6)]