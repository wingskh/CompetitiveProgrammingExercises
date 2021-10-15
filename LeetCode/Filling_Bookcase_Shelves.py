# https://leetcode.com/problems/filling-bookcase-shelves/submissions/
import math


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Assume that i is the last book of its level
        # Assume that j is the first book of the level if book i
        optimal_height = [math.inf for _ in range(len(books) + 1)]
        optimal_height[0] = 0

        for i in range(len(books)):
            acc_width = 0
            max_height = -1
            for j in range(i, -1, -1):
                if books[j][0] + acc_width <= shelfWidth:
                    acc_width += books[j][0]
                    max_height = max(max_height, books[j][1])
                    # optimal_height[j] + max_height as optimal_height starting from 1, len(books) + 1
                    # Therefore, optimal_height[j] -> the optimal height of last level of book i
                    optimal_height[i + 1] = min(
                        optimal_height[j] + max_height, optimal_height[i + 1]
                    )
                else:
                    break
        return optimal_height[-1]


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelf_width = 4
sol = Solution()
print(sol.minHeightShelves(books, shelf_width))
