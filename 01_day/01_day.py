import traceback

file = "input.in"

# Solución Reto 1
with open(file, 'r') as file:
    max_value = 0
    aux_max_value = 0
    for line in file:
        if line.strip():
            aux_max_value += int(line)
        else:
            max_value = max_value if max_value > aux_max_value else aux_max_value
            aux_max_value = 0
    print(max_value)
