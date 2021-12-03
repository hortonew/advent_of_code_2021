"""Power consumption can be found by multiplying gamma x epsilon."""
from typing import List


def convert_readings_to_frequency(readings: List[str]):
    d = {}
    for reading in readings:
        for idx, item in enumerate(reading):
            if idx+1 not in d:
                d[idx+1] = {'0': 0, '1': 0}

            if item == '0':
                d[idx+1]['0'] += 1
            else:
                d[idx+1]['1'] += 1

    return d

def calculate_gamma(readings: List[str]) -> int:
    d = convert_readings_to_frequency(readings)
    value = ''
    for _, v in d.items():
        value = f'{value}0' if v['0'] > v['1'] else f'{value}1'

    return int(value, 2)

def calculate_epsilon(readings: List[str]) -> int:
    d = convert_readings_to_frequency(readings)
    value = ''
    for _, v in d.items():
        value = f'{value}0' if v['0'] < v['1'] else f'{value}1'

    return int(value, 2)

def convert_file_to_list(file_name: str) -> List[str]:
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def main():
    readings = convert_file_to_list('3.txt')
    gamma = calculate_gamma(readings)
    epsilon = calculate_epsilon(readings)
    print(f'Final reading: {gamma=} x {epsilon=} = {gamma * epsilon}')

if __name__ == "__main__":
    main()
