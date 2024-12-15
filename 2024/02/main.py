
FILE_NAME = "input.txt"

def read_input(file_name: str):
    levels = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            levels.append(list(map(int, line.split(" "))))
    return levels

def compare_level(level: list[int], allow_mistake=False):
    last_diff = None
    for i in range(1, len(level)):
        n2 = level[i]
        n1 = level[i-1]
        diff = n2 - n1
        if abs(diff) == 0 or abs(diff) > 3 or (last_diff is not None and last_diff * diff < 0):
            if allow_mistake:
                for i in range(len(level)):
                    copy_level = level.copy()
                    copy_level.pop(i)
                    if compare_level(copy_level, allow_mistake=False):
                        return True
            return False
        
        if last_diff is None:
            last_diff = diff
    return True


def part_1(file: str):
    num_safe = 0
    levels = read_input(file)

    for idx in range(len(levels)):
        safe = compare_level(level=levels[idx])
        if safe:
            num_safe += 1
    return num_safe


def part_2(file: str):
    num_safe = 0
    levels = read_input(file)
    for idx in range(len(levels)):
        safe = compare_level(level=levels[idx], allow_mistake=True)
        if safe:
            num_safe += 1
    return num_safe


print(f"Num Safe Part 1: {part_1(FILE_NAME)}")
print(f"Num Safe Part 2: {part_2(FILE_NAME)}")