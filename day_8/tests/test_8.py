import pytest
from day_8.main_8_1 import convert_file_to_data, count_values_in_line


@pytest.fixture
def sample_line():
    return [
        'acedgfb',
        'cdfbe',
        'gcdfa',
        'fbcad',
        'dab',
        'cefabd',
        'cdfgeb',
        'eafb',
        'cagedb',
        'ab',
    ], ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']


@pytest.fixture
def sample_file(sample_line):
    return [sample_line, sample_line]


def test_8_1_convert_file_to_data(sample_file):
    data = convert_file_to_data('day_8/tests/sample.txt')
    assert data == sample_file


def test_8_1_count(sample_file):
    assert count_values_in_line(sample_file[0]) == 0
