import pytest
from day_7.main_7_1 import (calculate_fuel_cost, convert_file_to_data,
                            determine_alignment)


@pytest.fixture
def sample():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


test_data = [
    (2, 37),
    (1, 41),
    (3, 39),
    (10, 71),
]


def test_7_1_convert_file_to_horizontal_positions(sample):
    positions = convert_file_to_data('day_7/tests/sample.txt')
    assert positions == sample


def test_7_1_determine_alignment(sample):
    assert determine_alignment(sample) == 2


@pytest.mark.parametrize('alignment,expected_output', test_data)
def test_7_1_calculate_fuel_cost(alignment, expected_output, sample):
    assert calculate_fuel_cost(sample, alignment) == expected_output
