
def make_crate_stacks(lines):
    crate_stacks = [ [] for _ in range(9) ]
    for line in reversed(lines):
        crates = [line[i] for i in range(1, len(line), 4)]
        for i, crate in enumerate(crates):
            if crate != " ":
                crate_stacks[i].append(crate)
    return crate_stacks


def update_stacks(crate_stacks, instruction):
    number_of_moves, from_crate, to_crate = [int(s) for s in instruction.split() if s.isdigit()]
    for i in range(number_of_moves):
        lift_up = crate_stacks[from_crate-1].pop()
        crate_stacks[to_crate-1].append(lift_up)
    return crate_stacks


with open('puzzle_input.txt') as f:
    lines = f.readlines()
    crate_stacks = make_crate_stacks(lines[:8])
    instructions = lines[10:]
    for instruction in instructions:
        crate_stacks = update_stacks(crate_stacks, instruction)
    top_of_stack = [stack[-1] for stack in crate_stacks]
    print("".join(top_of_stack))