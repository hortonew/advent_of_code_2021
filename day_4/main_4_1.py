"""Giant Squid bingo game."""
import re
from dataclasses import dataclass
from typing import Any, List, Tuple


@dataclass
class Board:
    board: List[List[str]]


def convert_file_to_game_data(file_name: str) -> Tuple[List[str], List[Board]]:
    with open(file_name, 'r') as f:
        items = f.read().splitlines()

    boards: List[Board] = []
    inputs = items[0].split(',')

    # build boards
    in_board = False
    current_board: List[Any] = []
    for line in items[2:]:
        # In a group
        if not in_board:
            in_board = True
            current_board = []

        # Boards are separated by empty lines
        if len(line) > 0:
            # remove multiple spaces and split line into list of places
            row_to_add = re.sub(' +', ' ', line.strip()).split(' ')
            current_board.append(row_to_add)
        else:
            # Line should be ignored, but a task group may have ended
            boards.append(Board(current_board))
            in_board = False

    # Clean up if exiting due to end of file
    if in_board and current_board:
        boards.append(Board(current_board))

    return inputs, boards


def get_played_and_unplayed_numbers(
    board: Board, played_numbers: List[str]
) -> Tuple[List[str], List[str]]:
    # set of numbers that exist in the board
    all_board_numbers = {item for y in board.board for item in y}

    # only numbers that were both played and are in the board
    numbers_played_in_board = [
        num for num in played_numbers if num in all_board_numbers
    ]
    numbers_unplayed = [
        num for num in all_board_numbers if num not in played_numbers
    ]

    return list(numbers_played_in_board), list(numbers_unplayed)


def is_winning_board(board: Board, played_numbers: List[str]) -> bool:
    # empty board struct that will be filled out by what numbers were called
    board_struct: List[List[int]] = [
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [0] * 5,
    ]

    numbers_that_matter, _ = get_played_and_unplayed_numbers(
        board, played_numbers
    )

    # Build board structure based on what was called and what matters
    for row_idx, row in enumerate(board.board):
        for col_idx, column in enumerate(row):
            # print(f'{row_idx=}, {col_idx=}')
            if board.board[row_idx][col_idx] in numbers_that_matter:
                board_struct[row_idx][col_idx] = 1

    # We have a winner if any of the rows add up to 5 or more
    # return any(sum(row) >= 5 for row in board_struct)

    # Turn board on side to make it easier to sum the columns
    board_struct_on_side = [
        [row[0] for row in board_struct],
        [row[1] for row in board_struct],
        [row[2] for row in board_struct],
        [row[3] for row in board_struct],
        [row[4] for row in board_struct],
    ]

    # If 5 in a row (rows) or 5 in a row (columns), we have a winner
    return any(sum(row) >= 5 for row in board_struct) or any(
        sum(row) >= 5 for row in board_struct_on_side
    )


def get_answer(board: Board, played_numbers: List[str]) -> int:
    _, unplayed_numbers = get_played_and_unplayed_numbers(
        board, played_numbers
    )

    last_played = played_numbers[-1]
    print(f'{last_played=}')

    sum_of_unplayed = sum(int(x) for x in unplayed_numbers)
    print(f'{unplayed_numbers=}')
    print(f'{sum_of_unplayed=}')
    return int(last_played) * sum_of_unplayed


def play(inputs: List[str], list_of_boards: List[Board]) -> int:
    played_numbers: List[str] = []
    for input in inputs:
        played_numbers.append(input)
        if len(played_numbers) > 4:
            for board in list_of_boards:
                # A winning board needs 5 in a row, columns or rows (not diagonal)
                if is_winning_board(board, played_numbers):
                    # sum(played numbers) x last number called
                    # sum(board - played numbers) x played_numbers[-1]
                    return get_answer(board, played_numbers)

    return 0


def main():
    inputs, list_of_boards = convert_file_to_game_data('4.txt')
    winner = play(inputs, list_of_boards)
    print(f'Winner: {winner}')


if __name__ == '__main__':
    main()
