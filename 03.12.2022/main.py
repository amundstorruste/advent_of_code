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

