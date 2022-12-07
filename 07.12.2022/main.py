def do_recursive_jumbo(filereader, dir_sizes):
    dir_size = 0

    while True:
        line = filereader.readline()

        # Stop condition
        if line == "$ cd ..\n" or line == "":
            dir_sizes.append(dir_size)
            return dir_size

        # Add subdirectory size to directory size
        if line.split()[1] == "ls":
            dir_size+= do_recursive_jumbo(filereader, dir_sizes)
        
        # Add local files to directory size
        if line.split()[0].isdigit():
            dir_size += int(line.split()[0])
        

with open('puzzle_input.txt') as filereader:
    dir_sizes = []
    do_recursive_jumbo(filereader, dir_sizes)

    # Add up directories smaller than 100000
    task_a = sum(i for i in dir_sizes if i <= 100000)
    print(f"Task a): {task_a}")


# Identify availible space
with open('puzzle_input.txt') as filereader:
    filesize = 0
    while (True):
        line = filereader.readline()
        if line == "":
            break
        if line.split()[0].isdigit():
            filesize += int(line.split()[0])

filesystem = 70000000
required_space = 30000000

availible_space = filesystem - filesize
missing_space  = required_space - availible_space

potential_dirs = [i for i in dir_sizes if i >= missing_space]
task_b = min(potential_dirs)

print(f"Task b): {task_b}")