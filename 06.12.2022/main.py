
def identify_start_of_packet_marker(datastream):
    sequence = datastream[:4]
    for i in range(0, len(datastream)):
        if i < 4:
            continue
        sequence = datastream[i-4:i]
        if len(set(sequence)) == 4:
            return i, sequence
    return None

with open('puzzle_input.txt') as f:
    lines = f.readlines()
    datastream = lines[0]
    pos, marker = identify_start_of_packet_marker(datastream)
    print(pos, marker)