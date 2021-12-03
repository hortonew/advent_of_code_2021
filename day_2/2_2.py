# Multiply your final horizontal position by your final depth

horizontal_pos = 0
depth = 0
aim = 0

with open('2.txt', 'r') as f:
    for line in f:
        reading = line.split(' ')
        movement_type = reading[0]
        movement = int(reading[1])

        # aim
        if movement_type == 'down':
            aim += movement
        elif movement_type == 'up':
            aim -= movement

        # horizontal
        else:
            horizontal_pos += movement
            depth += aim * movement

print(
    f'With {horizontal_pos=} and {depth=}, final calculation is {horizontal_pos * depth}'
)
