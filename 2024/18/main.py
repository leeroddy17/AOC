from collections import deque

def read_input(file_name: str, n: int):
    grid = [["."] * n for _ in range(n)]
    with open(file_name, "r") as f:
        corrupted = [list(map(int, line.strip().split(","))) for line in f.readlines()]

        return grid, corrupted

def shortest_path(grid: list[list[str]]):
    ROWS = len(grid)
    COLS = len(grid[0])

    curr_step = 0
    queue = deque([(0, 0)])
    visited = set()    # maps coords -> min step

    for i in range(ROWS * COLS):
        to_visit = []

        if not queue:
            break

        while queue:
            x, y = queue.popleft()

            if x == ROWS - 1 and y == COLS - 1:
                return curr_step
            
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visited:
                continue
            
            if grid[x][y] == "#":
                continue
            
            visited.add((x, y))
            for x_, y_ in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                to_visit.append((x+x_, y+y_))
        
        for next in to_visit:
            queue.append(next)
        curr_step += 1

    return -1

def binary_search_first_closed(N: int, corrupted_bytes: list[list[int]]):
    left, right = 0, len(corrupted_bytes) - 1
    first_blocked = right
    while left <= right:
        mid = (left + right) // 2
        grid = [["."] * N for _ in range(N)]
        for x, y in corrupted_bytes[:mid+1]:
            grid[x][y] = "#"
        
        if shortest_path(grid) == -1:
            first_blocked = min(first_blocked, mid)
            right  = mid - 1
        else:
            left = mid + 1
    return corrupted_bytes[first_blocked]


# Part 1
print("Part 1: ")
g, corrupted_bytes = read_input("input.txt", n=71)
for i in range(1024):
    x, y = corrupted_bytes[i]
    g[x][y] = "#"
print(shortest_path(g))

# Part 2
print("Part 2: ")
g, corrupted_bytes = read_input("input.txt", n=71)
print(binary_search_first_closed(N=len(g), corrupted_bytes=corrupted_bytes))