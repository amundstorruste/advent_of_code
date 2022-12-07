def convert_char_to_val(char):
    asci_value = ord(char)
    if asci_value >= 97:
        return asci_value-96
    return asci_value-38


with open('puzzle_input') as f:
    lines = f.readlines()
    priority_list = []
    for line in lines:
        rucksack = line.rstrip()
        compartment_1 = rucksack[:len(rucksack)//2]
        compartment_2 = rucksack[len(rucksack)//2:]
        shared_char = "".join(set(compartment_1).intersection(compartment_2))
        value = convert_char_to_val(shared_char)
        priority_list.append(value)
    print(sum(priority_list))

with open('puzzle_input') as f:
    lines = f.readlines()
    badges = []
    squad_list = ["","",""]

    for i, line in enumerate(lines):
        rucksack = line.rstrip()

        squad_number = i % 3
        squad_list[squad_number] = rucksack
        
        if squad_number == 2:
            set_0 = set(squad_list[0])
            set_1 = set(squad_list[1])
            set_2 = set(squad_list[2])
            badge = set_0 & set_1 & set_2 
            badges.append("".join(badge))

    values = [convert_char_to_val(badge) for badge in badges]
    print(sum(values))
