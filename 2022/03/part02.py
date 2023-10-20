
with open("input.in", 'r') as file:
    lines = file.read().splitlines()
    total_sum = 0
    count = 0
    group = []
    aux = []
    for line in lines:
        count += 1
        if count % 3 == 0:
            aux.append(line)
            group.append(aux)
            # Check the priority of the group
            char_priority = next(iter(set(aux[0]).intersection(aux[1]).intersection(aux[2])))
            total_sum += ord(char_priority) - 96 if 'a' <= char_priority <= 'z' else ord(char_priority) - 38

            # Clean de aux list
            aux = []

        else:
            aux.append(line)

    print(f"PART 2: {total_sum}")
