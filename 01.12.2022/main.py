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
    print(f"Task a) {largest}")


with open('puzzle_input.txt') as f:
    lines = f.readlines()
    counter = 0
    largest_3 = [0, 0, 0]
    for line in lines:
        if line.isspace():
            if (counter > largest_3[0]):
                largest_3[0] = counter
                largest_3.sort()
            counter = 0
        else:
            counter += int(line) 
    print(f"Task b) {sum(largest_3)}")