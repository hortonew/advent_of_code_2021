import pytest
from day_4.main_4_1 import (
    Board,
    convert_file_to_game_data,
    is_winning_board,
    play,
)


@pytest.fixture
def sample():
    inputs = '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1'.split(
        ','
    )
    boards = []
    board1 = Board(
        [
            ['22', '13', '17', '11', '0'],
            ['8', '2', '23', '4', '24'],
            ['21', '9', '14', '16', '7'],
            ['6', '10', '3', '18', '5'],
            ['1', '12', '20', '15', '19'],
        ]
    )
    board2 = Board(
        [
            ['3', '15', '0', '2', '22'],
            ['9', '18', '13', '17', '5'],
            ['19', '8', '7', '25', '23'],
            ['20', '11', '10', '24', '4'],
            ['14', '21', '16', '12', '6'],
        ]
    )

    board3 = Board(
        [
            ['14', '21', '17', '24', '4'],
            ['10', '16', '15', '9', '19'],
            ['18', '8', '23', '26', '20'],
            ['22', '11', '13', '6', '5'],
            ['2', '0', '12', '3', '7'],
        ]
    )

    boards = [board1, board2, board3]
    return inputs, boards


def test_convert_file_to_game_data(sample):
    inputs, list_of_boards = convert_file_to_game_data(
        'day_4/tests/sample.txt'
    )
    assert inputs == sample[0]
    assert list_of_boards == sample[1]


def test_is_winning_board_by_row(sample):
    # check that board 1 would win with 5 numbers called
    assert is_winning_board(sample[1][0], ['22', '13', '17', '11', '0'])
    assert is_winning_board(sample[1][0], ['6', '10', '3', '18', '5'])
    assert is_winning_board(sample[1][2], ['22', '11', '13', '6', '5'])


def test_is_winning_board_by_column(sample):
    assert is_winning_board(sample[1][0], ['13', '2', '9', '10', '12'])


def test_play(sample):
    assert play(sample[0], sample[1]) == 4512
