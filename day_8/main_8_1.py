"""Seven Segment Search."""


from typing import List, Tuple


def convert_line(line: str) -> Tuple[List[str], List[str]]:
    """Convert line into Tuple of input and output lists."""
    io = line.split(' | ')
    i = io[0].split(' ')
    o = io[1].split(' ')
    return i, o


def convert_file_to_data(file_name: str) -> List[Tuple[List[str], List[str]]]:
    """Loads raw input."""
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    return [convert_line(line) for line in lines]


def count_values_in_line(line: Tuple[List[str], List[str]]) -> int:
    # 2 -> 1
    # 3 -> 7
    # 4 -> 4
    # 7 -> 8
    return sum(len(item) in [2, 3, 4, 7] for item in line[1])


def get_total(lines: List[Tuple[List[str], List[str]]]) -> int:
    return sum(count_values_in_line(line) for line in lines)


def main():
    """Raw input to list of items."""
    lines = convert_file_to_data('8.txt')
    print(get_total(lines))


if __name__ == '__main__':
    main()
