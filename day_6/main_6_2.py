"""Lanternfish."""


from copy import copy
from typing import Dict, List


def convert_file_to_data(file_name: str) -> Dict[int, int]:
    """Loads raw input into list of ints."""
    with open(file_name, 'r') as f:
        items = f.read().split(',')

    fish: List[int] = [int(i) for i in items]
    fish_summary: Dict[int, int] = {}

    for f in fish:  # type: ignore
        try:
            fish_summary[f] += 1  # type: ignore
        except KeyError:
            fish_summary[f] = 1  # type: ignore

    return fish_summary


def increment(fish_summary: Dict[int, int]) -> Dict[int, int]:
    new_fish: Dict[int, int] = {}
    school: Dict[int, int] = {}

    for f, value in fish_summary.items():
        # produce new fish
        if f == 0:
            try:
                school[6] += value
            except KeyError:
                school[6] = value

            try:
                new_fish[8] += value
            except Exception:
                new_fish[8] = value
        else:
            try:
                school[f - 1] += value
            except KeyError:
                school[f - 1] = value

    school.update(new_fish)
    return school


def simulate(fish: Dict[int, int], days: int) -> Dict[int, int]:
    """Simulate x number of days and return ending fish."""
    current_fish = copy(fish)
    for _ in range(days):
        current_fish = increment(current_fish)

    return current_fish


def get_fish_count(fish: Dict[int, int]) -> int:
    return sum(value for _, value in fish.items())


def main():
    """Raw input to list of items."""
    starting_fish = convert_file_to_data('6.txt')
    ending_fish = simulate(starting_fish, 256)

    print(f'Fish count: ending={get_fish_count(ending_fish)}')


if __name__ == '__main__':
    main()
