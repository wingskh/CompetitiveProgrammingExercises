# https://leetcode.com/problems/unique-paths-iii/
class Solution(object):
    def __init__(self):
        self.x_bound = 0
        self.y_bound = 0
        self.total_paths = 0
        self.total_counter = 0
        self.stack = []
        self.grid = None

    def uniquePathsIII(self, grid):
        """
        :type self.grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.x_bound = len(self.grid[0])
        self.y_bound = len(self.grid)
        start_coor = None
        for i in range(self.y_bound):
            for j in range(self.x_bound):
                if self.grid[i][j] == 1:
                    start_coor = (i, j)
                elif self.grid[i][j] == 0:
                    self.total_paths += 1

        self.find_num_of_path(start_coor)
        return self.total_counter

    def find_num_of_path(self, start_coor):
        top_coor = (start_coor[0]+1, start_coor[1])
        if top_coor[0] < self.y_bound:
            self.goto_one_direction(top_coor)

        bottom_coor = (start_coor[0]-1, start_coor[1])
        if bottom_coor[0] >= 0:
            self.goto_one_direction(bottom_coor)

        left_coor = (start_coor[0], start_coor[1]-1)
        if left_coor[1] >= 0:
            self.goto_one_direction(left_coor)

        right_coor = (start_coor[0], start_coor[1]+1)
        if right_coor[1] < self.x_bound:
            self.goto_one_direction(right_coor)

        if len(self.stack) != 0:
            self.stack.pop()

    def goto_one_direction(self,  new_coor):
        if self.grid[new_coor[0]][new_coor[1]] == 2:
            if len(self.stack) == self.total_paths:
                self.total_counter += 1
        elif self.grid[new_coor[0]][new_coor[1]] == 0 and new_coor not in self.stack:
            self.stack.append(new_coor)
            self.find_num_of_path(new_coor)
