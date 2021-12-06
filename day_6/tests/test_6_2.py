from copy import copy

import pytest
from day_6.main_6_2 import (
    convert_file_to_data,
    get_fish_count,
    increment,
    simulate,
)


@pytest.fixture
def sample():
    return {3: 2, 4: 1, 1: 1, 2: 1}


def test_6_2_convert_file_to_data(sample):
    fish = convert_file_to_data('day_6/tests/sample.txt')
    assert fish == sample


def test_6_2_increment(sample):
    assert increment(sample) == {2: 2, 3: 1, 0: 1, 1: 1}


def test_6_2_increment_2(sample):
    fish = copy(sample)
    fish = increment(fish)
    fish = increment(fish)
    assert fish == {1: 2, 2: 1, 6: 1, 0: 1, 8: 1}


def test_6_2_simulate(sample):
    ending_fish = simulate(sample, 18)
    assert get_fish_count(ending_fish) == 26


def test_6_2_simulate_2(sample):
    ending_fish = simulate(sample, 80)
    assert get_fish_count(ending_fish) == 5934


def test_6_2_simulate_3(sample):
    ending_fish = simulate(sample, 256)
    assert get_fish_count(ending_fish) == 26984457539
