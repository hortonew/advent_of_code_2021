# Measure increases (first one has no measurement)

previous_reading = None
current_reading = None
increases = 0

with open('1.txt', 'r') as f:
    for line in f:
        previous_reading = current_reading
        current_reading = int(line)

        if previous_reading and current_reading > previous_reading:
            increases += 1

print(increases)
