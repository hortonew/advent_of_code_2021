# Measure increases as groups of 3 (first one has no measurement)

previous_reading = None
current_reading = None
increases = 0
numbers = []

# Load file into list of integers
with open('1.txt', 'r') as f:
    for n in f:
        numbers.append(int(n.strip()))

for idx, number in enumerate(numbers):
    start = idx
    end = idx + 3
    number_range = numbers[start:end]

    previous_reading = current_reading
    current_reading = sum(number_range)

    if previous_reading and current_reading > previous_reading:
        increases += 1

print(increases)
