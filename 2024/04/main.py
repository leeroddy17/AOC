from enum import Enum

class Direction(Enum):
    UP = [0, 1]
    DOWN = [0, -1]
    FORWARD = [1, 0]
    BACKWARD = [-1, 0]
    UP_BACK = [-1, 1]
    UP_FRONT = [1, 1]
    DOWN_BACK = [-1, -1]
    DOWN_FRONT = [1, -1]

class Solution:
    def __init__(self, file_name: str, word: str):
        self._grid = self.read_input(file_name)
        self.ROWS = len(self._grid)
        self.COLS = len(self._grid[0])
        self.word = word
        self._all_directions = [
            Direction.UP, Direction.BACKWARD, Direction.FORWARD, Direction.DOWN, 
            Direction.UP_BACK, Direction.UP_FRONT, Direction.DOWN_BACK, Direction.DOWN_FRONT
        ]
        self.x_count = 0
        self.word_count = 0

    @property
    def grid(self):
        for line in self._grid:
            print(line)

    @staticmethod
    def read_input(file_name: str) -> list[list[str]]:
        grid = []
        with open(file_name, "r") as file:
            for line in file.readlines():
                grid.append(list(line.strip()))
        return grid
    
    def count_occurences(self):
        self.word_count = 0
        self.x_count = 0
        for row in range(self.ROWS):
            for col in range(self.COLS):
                # Part 1
                for direction in self._all_directions:
                    self.word_count += self.dfs(row, col, 0, direction)
                # Part 2
                self.x_count += self.count_x(row, col)

    def dfs(self, r: int, c: int, idx: int, direction: Direction):
        if idx == len(self.word):
            return 1
        if self.is_in_grid(r, c) and self._grid[r][c] == self.word[idx]:
            return self.dfs(r+direction.value[0], c+direction.value[1], idx+1, direction)
        else:
            return 0
        
    def is_in_grid(self, r: int, c: int) -> bool:
        return (0 <= r < self.ROWS) and (0 <= c < self.COLS)
        
    # Used in part 2, Hard Code to 'MAS'
    def count_x(self, r: int, c: int):
        if self._grid[r][c] != "A":
            return 0
        
        r1, c1 = r+Direction.DOWN_BACK.value[0], c+Direction.DOWN_BACK.value[1]
        r2, c2 = r+Direction.UP_FRONT.value[0], c+Direction.UP_FRONT.value[1]
        r3, c3 = r+Direction.DOWN_FRONT.value[0], c+Direction.DOWN_FRONT.value[1]
        r4, c4 = r+Direction.UP_BACK.value[0], c+Direction.UP_BACK.value[1]
        all_valid = self.is_in_grid(r1, c1) and self.is_in_grid(r2, c2) and self.is_in_grid(r3, c3) and self.is_in_grid(r4, c4)
        if all_valid and ((self._grid[r1][c1] == "M" and self._grid[r2][c2] == "S") \
            or (self._grid[r1][c1] == "S" and self._grid[r2][c2] == "M")) and ((self._grid[r3][c3] == "M" and self._grid[r4][c4] == "S") \
            or (self._grid[r3][c3] == "S" and self._grid[r4][c4] == "M")):
            return 1
        
        return 0

        
        
        
file_name = "input.txt"
word="XMAS"
c1 = Solution(file_name, word)
c1.count_occurences()
print(f"Number of Occurences of '{word}' in {file_name}: {c1.word_count}")

print(f"Number of Occurences of 'MAX' as 'X' in {file_name}: {c1.x_count}")
