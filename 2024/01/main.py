from collections import Counter

def read_lists():
    l1 = []
    l2 = []

    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            n1, n2 = line.split("   ")
            l1.append(int(n1))
            l2.append(int(n2))
    return l1, l2

def part_1():
    l1, l2 = read_lists()
    l1.sort()
    l2.sort()

    res = 0
    for n1, n2 in zip(l1, l2):
        res += abs(n1-n2)
    return res

def part_2():
    l1, l2 = read_lists()
    c2 = Counter(l2)

    res = 0
    for num in l1:
        res += num * c2.get(num, 0)
    return res


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")