"""The Treachery of Whales."""


from typing import List


def convert_file_to_data(file_name: str) -> List[int]:
    """Loads raw input into list of ints."""
    with open(file_name, 'r') as f:
        positions = f.read().split(',')

    return [int(i) for i in positions]


def determine_alignment(horizontal_positions: List[int]) -> int:
    horizontal_positions.sort()
    lowerbound = min(horizontal_positions)
    upperbound = max(horizontal_positions)
    minimum_fuel = calculate_fuel_cost(horizontal_positions, upperbound)
    alignment = lowerbound

    for i in range(alignment, upperbound + 1):
        current = calculate_fuel_cost(horizontal_positions, i)
        if current < minimum_fuel:
            minimum_fuel = current
            alignment = i
    return alignment


def calculate_fuel_cost(
    horizontal_positions: List[int], alignment: int
) -> int:

    total = 0
    for position in horizontal_positions:
        distance = abs(position - alignment)
        fuel_costs = sum(list(range(1, distance + 1)))
        total += fuel_costs

    return total


def main():
    """Raw input to list of items."""
    horizontal_positions = convert_file_to_data('7.txt')
    alignment = determine_alignment(horizontal_positions)
    fuel_cost = calculate_fuel_cost(horizontal_positions, alignment)
    print(fuel_cost)


if __name__ == '__main__':
    main()
