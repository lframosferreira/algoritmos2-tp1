from src.point.point import Point
from src.segment.segment import Segment


def test_is_counter_clockwise():
    data: list[list[int]] = [
        [1, 1, 2, 2, 3, 4],
        [7, 0, 4, 2, 0, 3],
        [2, -4, 6, -4, 7, 1],
        [-6, 2, -8, -1, -5, -4],
        [2, 1, 4, 4, 2, 6],
    ]
    for case in data:
        points: list[Point] = [
            Point(case[0], case[1]),
            Point(case[2], case[3]),
            Point(case[4], case[5]),
        ]
        segments: list[Segment] = [
            Segment(points[0], points[1]),
            Segment(points[1], points[2]),
        ]

        assert segments[0].is_counter_clockwise(segments[1]) == False
        assert segments[1].is_counter_clockwise(segments[0]) == True
