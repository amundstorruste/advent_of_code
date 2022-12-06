
with open('puzzle_input') as f:
    lines = f.readlines()
    count_fully_contained = 0
    for line in lines:
        assignments = line.rstrip().split(",")
        section_1, section_2 = map(int, assignments[0].split("-"))
        section_3, section_4 = map(int, assignments[1].split("-"))
        if section_1 <= section_3 and section_4 <= section_2:
            count_fully_contained += 1
            continue
        if section_3 <= section_1 and section_2 <= section_4:
            count_fully_contained += 1
    print(count_fully_contained)
