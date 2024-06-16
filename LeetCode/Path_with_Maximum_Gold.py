# https://leetcode.com/problems/path-with-maximum-gold
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def is_valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 0
        
        def dfs(r, c):
            cur_gold = grid[r][c]
            grid[r][c] = 0
            acc_gold = cur_gold
            for next_r, next_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if is_valid(next_r, next_c):
                    acc_gold = max(acc_gold, cur_gold + dfs(next_r, next_c))
            grid[r][c] = cur_gold
            return acc_gold

        max_gold = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, dfs(r, c))

        return max_gold

# grid = [
#     [0,6,0],
#     [5,8,7],
#     [0,9,0],
# ]
# Output: 24
# grid = [
#     [1,0,7],
#     [2,0,6],
#     [3,4,5],
#     [0,3,0],
#     [9,0,20],
# ]
# Output: 28
# grid = [
#     [1,0,7,0,0,0],
#     [2,0,6,0,1,0],
#     [3,5,6,7,4,2],
#     [4,3,1,0,2,0],
#     [3,0,5,0,20,0],
# ]
# Output: 60
grid = [
    [0,0,0,0,0,0,32,0,0,20],
    [0,0,2,0,0,0,0,40,0,32],
    [13,20,36,0,0,0,20,0,0,0],
    [0,31,27,0,19,0,0,25,18,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,18,0,6],
    [0,0,0,25,0,0,0,0,0,0],
    [0,0,0,21,0,30,0,0,0,0],
    [19,10,0,0,34,0,2,0,0,27],
    [0,0,0,0,0,34,0,0,0,0],
]
# Output: 129
sol = Solution()
result = sol.getMaximumGold(grid)
print(result)