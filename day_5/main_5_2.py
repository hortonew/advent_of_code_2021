"""Hydrothermal Venture."""
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Coordinate:
    x: int
    y: int


def is_line(coordinate_1: Coordinate, coordinate_2: Coordinate):
    """Return true if x1==x2, or y1==y2 match."""
    return coordinate_1.x == coordinate_2.x or coordinate_1.y == coordinate_2.y


def is_diagonal(x1: int, x2: int, y1: int, y2: int) -> bool:
    """Calculate slope and if 1 return True."""
    x_max = max(x1, x2)
    x_min = min(x1, x2)
    y_max = max(y1, y2)
    y_min = min(y1, y2)
    try:
        slope = abs((y_max - y_min) / (x_max - x_min))
    except ZeroDivisionError:
        # 0/0 is still slope of 1
        return True

    # If slope is 1 we have a diagonal point
    return slope == 1


def get_coordinates_from_range(
    coordinate_1: Coordinate, coordinate_2: Coordinate
) -> List[Coordinate]:
    """Return list of coordinates that fall in range."""
    '''
    Return list of coordinates that fall in range.

    Example:
        1,1 -> 1,3: Returns [(1, 1), (1, 2), (1, 3)]
        9,7 -> 7,7: Returns [(9, 7), (8, 7), (7, 7)]
    '''
    start_x = coordinate_1.x
    start_y = coordinate_1.y
    end_x = coordinate_2.x
    end_y = coordinate_2.y
    points: List[Coordinate] = []

    if start_x == end_x:
        # do y line
        begin = min(start_y, end_y)
        end = max(start_y, end_y)
        point_range = list(range(begin, end)) + [end]

        if begin == end_y:
            point_range.reverse()
        for point in point_range:
            points.append(Coordinate(start_x, point))
    elif start_y == end_y:
        # do x line
        begin = min(start_x, end_x)
        end = max(start_x, end_x)
        point_range = list(range(begin, end)) + [end]

        if begin == end_x:
            point_range.reverse()
        for point in point_range:
            points.append(Coordinate(point, start_y))
    else:
        # return single point as they're equal
        return [Coordinate(start_x, end_y)]

    return points


def get_diagonal_coordinates_from_range(
    coordinate_1: Coordinate, coordinate_2: Coordinate
) -> List[Coordinate]:
    """Maps range of coordinates stepping diagonally."""

    start_x = coordinate_1.x
    start_y = coordinate_1.y
    end_x = coordinate_2.x
    end_y = coordinate_2.y
    points: List[Coordinate] = []

    if start_x == end_x and start_y == end_y:
        return [Coordinate(start_x, end_y)]

    # x list
    if start_x > end_x:
        x_range = list(range(start_x, end_x, -1)) + [end_x]
    else:
        x_range = list(range(start_x, end_x)) + [end_x]

    # y list
    if start_y > end_y:
        y_range = list(range(start_y, end_y, -1)) + [end_y]
    else:
        y_range = list(range(start_y, end_y)) + [end_y]

    for item in zip(x_range, y_range):
        points.append(Coordinate(item[0], item[1]))

    return points


def convert_file_to_data(file_name: str):
    """Loads raw input into list."""
    with open(file_name, 'r') as f:
        items = f.read().splitlines()

    return items


def create_coordinate_tuple_from_raw(
    input: str,
) -> Tuple[Coordinate, Coordinate]:
    """Take raw input and convert into two coordinates."""
    parse = input.split(' -> ')
    c1 = parse[0].split(',')
    c2 = parse[1].split(',')
    return Coordinate(int(c1[0]), int(c1[1])), Coordinate(
        int(c2[0]), int(c2[1])
    )


def convert_raw_input_to_acceptable_points(
    raw_ranges: List[str],
) -> List[Coordinate]:
    """Builds list of acceptable data points that meet criteria."""
    acceptable_points: List[Coordinate] = []
    for range in raw_ranges:
        c1, c2 = create_coordinate_tuple_from_raw(range)
        if is_line(c1, c2):
            # calculate all horizontal/vertical points
            points = get_coordinates_from_range(c1, c2)
        elif is_diagonal(c1.x, c2.x, c1.y, c2.y):
            # calculate all diagonal points
            points = get_diagonal_coordinates_from_range(c1, c2)

        for point in points:
            acceptable_points.append(point)

    return acceptable_points


def get_count_of_overlapping_points(coordinates: List[Coordinate]) -> int:
    """Measures how many points overlap more than once."""
    counts: Dict[str, int] = {}
    for coordinate in coordinates:
        try:
            counts[f'{coordinate.x},{coordinate.y}'] += 1
        except KeyError:
            counts[f'{coordinate.x},{coordinate.y}'] = 1

    return sum(value >= 2 for point, value in counts.items())


def main():
    """Return count of locations that have at least two numbers overlapping."""
    # raw input to list of items
    raw_input = convert_file_to_data('5.txt')

    # list of items to range of coordinates
    acceptable_points = convert_raw_input_to_acceptable_points(raw_input)
    count_of_overlapping_points = get_count_of_overlapping_points(
        acceptable_points
    )
    print(count_of_overlapping_points)


if __name__ == '__main__':
    main()
