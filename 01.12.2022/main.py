a = 1

with open('puzzle_input.txt') as f:
    lines = f.readlines()
    counter = 0
    largest = 0
    for line in lines:
        if line.isspace():
            if (counter >= largest):
                largest = counter
            counter = 0
        else:
            counter += int(line) 
    print(largest)