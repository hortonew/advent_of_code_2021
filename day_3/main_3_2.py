"""Power consumption can be found by multiplying gamma x epsilon."""
from copy import copy
from typing import Any, List


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

def calculate_oxygen_generator_rating(readings: List[str]) -> Any:
    idx = 1
    value = ''
    r = copy(readings)
    while len(r) != 1:
        d = convert_readings_to_frequency(r)
        value = f'{value}0' if d[idx]['0'] > d[idx]['1'] else f'{value}1'

        # If items don't begin with what we want, throw them away
        items_to_remove = [reading for reading in r if not reading.startswith(value)]
        for item in items_to_remove:
            r.remove(item)
        idx+=1

    return int(r[0], 2)

def calculate_co2_scrubber_rating(readings: List[str]) -> Any:
    idx = 1
    value = ''
    r = copy(readings)
    while len(r) != 1:
        d = convert_readings_to_frequency(r)
        value = f'{value}0' if d[idx]['0'] <= d[idx]['1'] else f'{value}1'
        # value = f'{value}0' if v['0'] < v['1'] else f'{value}1'

        # If items don't begin with what we want, throw them away
        items_to_remove = [reading for reading in r if not reading.startswith(value)]
        for item in items_to_remove:
            r.remove(item)
        idx+=1

    return int(r[0], 2)

def convert_file_to_list(file_name: str) -> List[str]:
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def main():
    readings = convert_file_to_list('3.txt')
    oxygen = calculate_oxygen_generator_rating(readings)
    c02 = calculate_co2_scrubber_rating(readings)
    print(f'Final reading: {oxygen=} x {c02=} = {oxygen * c02}')

if __name__ == "__main__":
    main()
