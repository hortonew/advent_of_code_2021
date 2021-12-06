"""Lanternfish."""


from copy import copy
from typing import List


def convert_file_to_data(file_name: str) -> List[int]:
    """Loads raw input into list of ints."""
    with open(file_name, 'r') as f:
        items = f.read().split(',')

    return [int(i) for i in items]


def increment(fish: List[int]) -> List[int]:
    new_fish: List[int] = []
    school: List[int] = []

    for f in fish:
        # produce new fish
        if f == 0:
            school.append(6)
            new_fish.append(8)
        else:
            school.append(f - 1)

    school += new_fish
    return school


def simulate(fish: List[int], days: int) -> List[int]:
    """Simulate x number of days and return ending fish."""
    current_fish = copy(fish)
    for _ in range(days):
        current_fish = increment(current_fish)

    return current_fish


def main():
    """Raw input to list of items."""
    starting_fish = convert_file_to_data('6.txt')
    ending_fish = simulate(starting_fish, 80)
    print(
        f'Fish count: starting={len(starting_fish)}, ending={len(ending_fish)}'
    )


if __name__ == '__main__':
    main()
