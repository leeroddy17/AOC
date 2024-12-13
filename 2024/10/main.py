

def read_input():
    grid = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            grid.append(list(map(int, line)))
    return grid
    

def get_sum_trailheads(grid: list[list[int]]):
    total_num_trailheads = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(row, col, current, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid) or (row, col) in visited or grid[row][col] != current:
            return 0
        
        if current == 0 and grid[row][col] == current and (row, col) not in visited:
            visited.add((row, col))
            return 1
        
        total_paths = dfs(row+1, col, current-1, visited) + dfs(row-1, col, current-1, visited) + dfs(row, col+1, current-1, visited) + dfs(row, col-1, current-1, visited)
        return total_paths

    for row in range(ROWS):
        for col in range(COLS):
            total_num_trailheads += dfs(row, col, 9, set())
    return total_num_trailheads


def get_sum_ratings(grid: list[list[int]]):
    total_num_trailheads = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(row, col, current, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid) or (row, col) in visited or grid[row][col] != current:
            return 0
        
        if current == 0 and grid[row][col] == current and (row, col) not in visited:
            return 1
        
        visited.add((row, col))
        total_paths = dfs(row+1, col, current-1, visited) + dfs(row-1, col, current-1, visited) + dfs(row, col+1, current-1, visited) + dfs(row, col-1, current-1, visited)
        visited.remove((row, col))
        return total_paths

    for row in range(ROWS):
        for col in range(COLS):
            total_num_trailheads += dfs(row, col, 9, set())
    return total_num_trailheads


grid = read_input()
print(get_sum_trailheads(grid))
print(get_sum_ratings(grid))