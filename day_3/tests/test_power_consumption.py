import pytest
from day_3.main_3_1 import (calculate_epsilon, calculate_gamma,
                            convert_file_to_list)
from day_3.main_3_2 import (calculate_co2_scrubber_rating,
                            calculate_oxygen_generator_rating)


@pytest.fixture
def sample():
    return [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

def test_convert_file_to_list(sample):
    result = convert_file_to_list('day_3/tests/sample.txt')
    assert result == sample


def test_gamma_rate(sample):
    gamma = calculate_gamma(sample)
    assert gamma == 22

def test_epsilon_rate(sample):
    epsilon = calculate_epsilon(sample)
    assert epsilon == 9


def test_calculate_oxygen_generator_rating(sample):
    oxygen = calculate_oxygen_generator_rating(sample)
    assert oxygen == 23

def test_calculate_c02(sample):
    c02 = calculate_co2_scrubber_rating(sample)
    assert c02 == 10
