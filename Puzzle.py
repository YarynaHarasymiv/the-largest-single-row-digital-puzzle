from collections import defaultdict


with open('source.txt', 'r') as file:
    puzzle = [line.strip() for line in file]


part_dict = defaultdict(list)
for part in puzzle:
    first_two = part[:2]
    last_two = part[-2:]
    part_dict[last_two].append(part)


def find_longest_path(current_part, visited):
    visited.add(current_part)
    max_way = [current_part]
    last_two = current_part[-2:]
    for next_part in part_dict[last_two]:
        if next_part not in visited:
            way = find_longest_path(next_part, visited.copy())
            if len(way) > len(max_way):
                max_way = [current_part] + way
    return max_way


longest_sequence = []
for part in puzzle:
    way = find_longest_path(part, set())
    if len(way) > len(longest_sequence):
        longest_sequence = way


if longest_sequence:
    result = longest_sequence[0]
    for part in longest_sequence[1:]:
        result += part[2:]
    print("The longest sequence:", result)
else:
    print("No sequence found.")
