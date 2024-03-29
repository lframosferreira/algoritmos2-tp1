# pylint: disable=missing-function-docstring, missing-module-docstring

from numpy import Inf

from src.point import Point
from src.segment import Segment


def test_is_counter_clockwise() -> None:
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

        assert not segments[0].is_counter_clockwise(segments[1])
        assert segments[1].is_counter_clockwise(segments[0])


def test_invert() -> None:
    seg: Segment = Segment(Point(1, 4), Point(2, 3))
    seg.invert()
    assert seg.p0 == Point(2, 3)
    assert seg.p1 == Point(1, 4)


def test_contains() -> None:
    seg: Segment = Segment(Point(1, 2), Point(3, 4))
    assert seg.contains(Point(2, 3))  # Na linha
    assert not seg.contains(Point(3, 6))  # Acima de um extremo
    assert not seg.contains(Point(3, 5))  # No extremo
    assert not seg.contains(Point(0, 1))  # Esquerda


def test_orientation() -> None:
    seg: Segment = Segment(Point(0, 0), Point(3, 0))

    clockwise: int = seg.orientation(Point(5, -3))
    assert clockwise == 1

    counterclockwise: int = seg.orientation(Point(2, 1))
    assert counterclockwise == -1

    colinear: int = seg.orientation(Point(1, 0))
    assert colinear == 0


def test_intersects() -> None:
    seg1: Segment = Segment(Point(1, 6), Point(5, 7))
    seg2: Segment = Segment(Point(2, 5), Point(4, 9))
    seg3: Segment = Segment(Point(2, 2), Point(4, 6))
    seg4: Segment = Segment(Point(3, 7), Point(5, 8))
    seg5: Segment = Segment(Point(5, 8), Point(9, 9))

    # Compartilham um ponto
    assert seg4.intersects(seg5)

    # Mesmo segmento
    assert seg1.intersects(seg1)

    # Ambas orientações trocados
    assert seg1.intersects(seg2)

    # Colinearidade
    assert seg2.intersects(seg4)

    # Não há interseção
    assert not seg1.intersects(seg3)

    # Colinearidade "fora"
    assert not seg3.intersects(seg5)


def test_perpendicular_segment() -> None:

    seg_simple: Segment = Segment(Point(1, 1), Point(3, 3))
    slope, coef, midpoint = seg_simple.get_perpendicular_segment()

    assert midpoint == Point(2, 2)
    assert slope == -1
    assert coef == 4

    seg_vertical: Segment = Segment(Point(1, 1), Point(1, 3))
    slope, coef, midpoint = seg_vertical.get_perpendicular_segment()
    assert midpoint == Point(1, 2)
    assert slope == 0
    assert coef == 2

    seg_horizontal: Segment = Segment(Point(1, 1), Point(5, 1))
    slope, coef, midpoint = seg_horizontal.get_perpendicular_segment()
    assert midpoint == Point(3, 1)
    assert slope == Inf
    assert coef == 3
