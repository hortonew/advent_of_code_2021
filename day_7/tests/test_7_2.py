import pytest
from day_7.main_7_2 import (
    calculate_fuel_cost,
    convert_file_to_data,
    determine_alignment,
)


@pytest.fixture
def sample():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


test_data = [
    (2, 206),
]

test_data_single = [
    ([16], 5, 66),
    ([1], 5, 10),
    ([2], 5, 6),
    ([0], 5, 15),
    ([4], 5, 1),
    ([2], 5, 6),
    ([7], 5, 3),
    ([1], 5, 10),
    ([2], 5, 6),
    ([14], 5, 45),
]


def test_7_2_convert_file_to_horizontal_positions(sample):
    positions = convert_file_to_data('day_7/tests/sample.txt')
    assert positions == sample


def test_7_2_determine_alignment(sample):
    assert determine_alignment(sample) == 5


@pytest.mark.parametrize('alignment,expected_output', test_data)
def test_7_2_calculate_fuel_cost(alignment, expected_output, sample):
    assert calculate_fuel_cost(sample, alignment) == expected_output


def test_7_2_test_single():
    assert calculate_fuel_cost([2], 5) == 6


@pytest.mark.parametrize('crabs,alignment,expected_output', test_data_single)
def test_7_2_calculate_fuel_cost_single(crabs, alignment, expected_output):
    assert calculate_fuel_cost(crabs, alignment) == expected_output
