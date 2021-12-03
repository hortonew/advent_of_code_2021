import pytest
from day_3.main_3_1 import (calculate_epsilon, calculate_gamma,
                            convert_file_to_list)

d = {1: {'0': 0, '1': 5}, 2: {'0': 0, '1': 5}, 3: {'0': 0, '1': 5}, 4: {'0': 0, '1': 5}, 5: {'0': 0, '1': 5}, 6: {'0': 0, '1': 5}, 7: {'0': 0, '1': 5}, 8: {'0': 0, '1': 5}, 9: {'0': 0, '1': 5}, 10: {'0': 0, '1': 5}, 11: {'0': 0, '1': 5}, 12: {'0': 0, '1': 5}}

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
