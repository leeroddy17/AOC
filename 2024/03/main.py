import re

FILE_NAME = "input.txt"

def read_input(fn):
    with open(fn, 'r') as file:
        return file.read()
    
def part_1(fn):
    input_string = read_input(fn)
    pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    all_items = re.findall(pattern, input_string)
    res = 0
    for item in all_items:
        res += int(item[0]) * int(item[1])
    return res

def part_2(fn):
    input_string = read_input(fn)
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    all_instructions = re.findall(pattern, input_string)

    res = 0
    mult_on = True
    for item in all_instructions:
        if item == "do()":
            mult_on = True
        elif item == "don't()":
            mult_on = False
        else:
            nums = re.findall(r'\d{1,3}', item)
            res += int(nums[0]) * int(nums[1]) if mult_on else 0
    return res


print(f"Part 1 Solution: {part_1(FILE_NAME)}")
print(f"Part 2 Solution: {part_2(FILE_NAME)}")