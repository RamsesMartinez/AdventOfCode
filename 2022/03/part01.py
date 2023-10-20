
with open("input.in", 'r') as file:
    lines = file.read().splitlines()
    total_sum = 0
    for line in lines:
        mid_size = len(line)//2
        set_a, set_b = set(line[:mid_size]), set(line[mid_size:])
        char = next(iter(set_a.intersection(set_b)))
        total_sum += ord(char) - 96 if 'a' <= char <= 'z' else ord(char) - 38
    print(f"PART 1: {total_sum}")
