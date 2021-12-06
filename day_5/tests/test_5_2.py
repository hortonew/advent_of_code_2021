import pytest
from day_5.main_5_2 import (
    Coordinate,
    convert_file_to_data,
    convert_raw_input_to_acceptable_points,
    create_coordinate_tuple_from_raw,
    get_coordinates_from_range,
    get_count_of_overlapping_points,
    is_diagonal,
)


@pytest.fixture
def sample():
    return [
        '0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2',
    ]


@pytest.fixture
def acceptable_points():
    return [
        # 0, 9 -> 5, 9
        Coordinate(0, 9),
        Coordinate(1, 9),
        Coordinate(2, 9),
        Coordinate(3, 9),
        Coordinate(4, 9),
        Coordinate(5, 9),
        # 8, 0 -> 0, 8
        Coordinate(8, 0),
        Coordinate(7, 1),
        Coordinate(6, 2),
        Coordinate(5, 3),
        Coordinate(4, 4),
        Coordinate(3, 5),
        Coordinate(2, 6),
        Coordinate(1, 7),
        Coordinate(0, 8),
        # 9, 4 -> 3, 4
        Coordinate(9, 4),
        Coordinate(8, 4),
        Coordinate(7, 4),
        Coordinate(6, 4),
        Coordinate(5, 4),
        Coordinate(4, 4),
        Coordinate(3, 4),
        # 2, 2 -> 2, 1
        Coordinate(2, 2),
        Coordinate(2, 1),
        # 7, 0 -> 7, 4
        Coordinate(7, 0),
        Coordinate(7, 1),
        Coordinate(7, 2),
        Coordinate(7, 3),
        Coordinate(7, 4),
        # 6, 4 -> 2, 0
        Coordinate(6, 4),
        Coordinate(5, 3),
        Coordinate(4, 2),
        Coordinate(3, 1),
        Coordinate(2, 0),
        # 0, 9 -> 2, 9
        Coordinate(0, 9),
        Coordinate(1, 9),
        Coordinate(2, 9),
        # 3, 4 -> 1, 4
        Coordinate(3, 4),
        Coordinate(2, 4),
        Coordinate(1, 4),
        # 0, 0 -> 8, 8
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
        Coordinate(4, 4),
        Coordinate(5, 5),
        Coordinate(6, 6),
        Coordinate(7, 7),
        Coordinate(8, 8),
        # 5, 5 -> 8, 2
        Coordinate(5, 5),
        Coordinate(6, 4),
        Coordinate(7, 3),
        Coordinate(8, 2),
    ]


def test_5_2_convert_file_to_data(sample):
    raw_input = convert_file_to_data('day_5/tests/sample.txt')
    assert raw_input == sample


def test_5_2_create_coordinate_tuple_from_raw():
    raw_input = '0,9 -> 5,9'
    c1, c2 = create_coordinate_tuple_from_raw(raw_input)
    assert c1 == Coordinate(0, 9)
    assert c2 == Coordinate(5, 9)


def test_5_2_get_coordinates_from_range():
    c1 = Coordinate(1, 1)
    c2 = Coordinate(1, 3)
    points = get_coordinates_from_range(c1, c2)
    assert points == [
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(1, 3),
    ]


def test_5_2_get_coordinates_from_range_2():
    c1 = Coordinate(9, 7)
    c2 = Coordinate(7, 7)
    points = get_coordinates_from_range(c1, c2)
    assert points == [
        Coordinate(9, 7),
        Coordinate(8, 7),
        Coordinate(7, 7),
    ]


def test_5_2_get_coordinates_from_range_3():
    c1 = Coordinate(0, 4)
    c2 = Coordinate(0, 1)
    points = get_coordinates_from_range(c1, c2)
    assert points == [
        Coordinate(0, 4),
        Coordinate(0, 3),
        Coordinate(0, 2),
        Coordinate(0, 1),
    ]


def test_5_2_convert_raw_input_to_acceptable_points(sample, acceptable_points):
    assert convert_raw_input_to_acceptable_points(sample) == acceptable_points


def test_5_2_get_count_of_overlapping_points():
    assert (
        get_count_of_overlapping_points([Coordinate(1, 1), Coordinate(1, 1)])
        == 1
    )


def test_5_2_is_diagonal():
    assert is_diagonal(1, 1, 3, 3)
    assert is_diagonal(3, 3, 1, 1)
    assert is_diagonal(9, 7, 7, 9)


def test_5_2_get_count_of_overlapping_points_sample(acceptable_points):
    assert get_count_of_overlapping_points(acceptable_points) == 12
