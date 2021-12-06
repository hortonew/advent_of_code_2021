from copy import copy

import pytest
from day_6.main_6_1 import convert_file_to_data, increment, simulate


@pytest.fixture
def sample():
    return [3, 4, 3, 1, 2]


def test_6_1_convert_file_to_data(sample):
    fish = convert_file_to_data('day_6/tests/sample.txt')
    assert fish == sample


def test_6_1_increment(sample):
    assert increment(sample) == [2, 3, 2, 0, 1]


def test_6_1_increment_2(sample):
    fish = copy(sample)
    fish = increment(fish)
    fish = increment(fish)
    assert fish == [1, 2, 1, 6, 0, 8]


def test_6_1_simulate(sample):
    ending_fish = simulate(sample, 18)
    assert len(ending_fish) == 26


def test_6_1_simulate_2(sample):
    ending_fish = simulate(sample, 80)
    assert len(ending_fish) == 5934
