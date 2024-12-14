from collections import defaultdict, deque
import re

class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self, num_seconds: int, width: int, height: int):
        for _ in range(num_seconds):
            self.px += self.vx
            self.py += self.vy

            if self.px >= 0:
                self.px %= width
            else:
                self.px += width

            if self.py >= 0:
                self.py %= height
            else:
                self.py += height
    

class Solution:
    def __init__(self, width: int, height: int):
        self.WIDTH = width
        self.HEIGHT = height
        self.robots: list[Robot] = []
        
        # self.read_input(file_name)
        # self.grid: list[list[int]] = self.init_grid()
        
    def read_input(self, file_name: str):
        pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
        with open(file_name, "r") as file:
            content = file.read()
            for match in re.finditer(pattern, content):
                px, py, vx, vy = map(int, match.groups())
                self.robots.append(Robot(px, py, vx, vy))
                # print(px, py, vx, vy)
        # print("Read in ", len(self.robots), " robots")

    def init_grid(self) -> list[list[int]]:
        grid = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        for robot in self.robots:
            grid[robot.py][robot.px] += 1
        return grid

    def simulate(self, num_iter: int):
        for robot in self.robots:
            robot.move(num_iter, self.WIDTH, self.HEIGHT)

    def get_safety_factor(self, grid: list[list[int]]):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        mid_width = self.WIDTH // 2
        mid_height = self.HEIGHT // 2
        for r in range(self.HEIGHT):
            for c in range(self.WIDTH):
                if r == mid_height or c == mid_width:
                    continue
                elif r > mid_height and c > mid_width:
                    q4 += grid[r][c]
                elif r < mid_height and c > mid_width:
                    q3 += grid[r][c]
                elif r < mid_height and c < mid_width:
                    q2 += grid[r][c]
                else:
                    q1 += grid[r][c]
        return (q1*q2*q3*q4)



# Example
c = Solution(width=11, height=7)
c.read_input("test.txt")
# c.init_grid()
c.simulate(100)
print(c.get_safety_factor(c.init_grid()))
# c.show()


# Input Solution
c = Solution(width=101, height=103)
c.read_input("input.txt")
# c.init_grid()
c.simulate(100)
print(c.get_safety_factor(c.init_grid()))

print("Part 2 (TODO:)")