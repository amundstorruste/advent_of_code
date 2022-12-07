def do_recursive_jumbo(filereader, dir_sizes):
    dir_size = 0

    while True:
        # find dir_size
        line = filereader.readline()

        if line == "":
            break

        if line.split()[1] == "ls":
            sub_folder_size = do_recursive_jumbo(filereader, dir_sizes)
            dir_size+= sub_folder_size
        # Else we have either a dir or a filesize
        
        if line.split()[0] != "$" and line.split()[0] != "dir":
            dir_size += int(line.split()[0])
        
        if line == "$ cd ..\n":
            break
    dir_sizes.append(dir_size)
    return dir_size


with open('puzzle_input.txt') as filereader:
    # lines = f.readlines()

    # Find size of all dictionaries
    isCounting = False
    dir_sizes = []
    while (True):
        line = filereader.readline()
        if line == "":
            break
        if line.split()[1] == "ls":
            do_recursive_jumbo(filereader, dir_sizes)

    print("done")

    # Add up
    res = sum(i for i in dir_sizes if i <= 100000)
    print(res)

    total_size = sum(dir_sizes)
    print(total_size)

# Identify availible space
with open('puzzle_input.txt') as filereader:
    filesize = 0
    while (True):
        line = filereader.readline()
        if line == "":
            break
        if line.split()[0] != "$" and line.split()[0] != "dir":
            filesize += int(line.split()[0])

    print(f"filesize: {filesize}")

filesystem = 70000000
required_space = 30000000

space = filesystem - filesize
required_deletion  = required_space - space

potential_dirs = [i for i in dir_sizes if i >= required_deletion]
best_option = min(potential_dirs)

print(best_option)