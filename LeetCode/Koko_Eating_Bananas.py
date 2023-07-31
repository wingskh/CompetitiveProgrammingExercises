# https://leetcode.com/problems/koko-eating-bananas/
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_finished_hour(k):
            return sum([math.ceil(pile/k) for pile in piles])
        
        left_index, right_index = 1, max(piles)

        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            finished_hour = get_finished_hour(middle_index)
            print(left_index , right_index, finished_hour)
            if finished_hour > h:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

        return left_index


piles = [312884470]
h = 312884469
piles = [3,6,7,11]
h = 8
sol = Solution()
result = sol.minEatingSpeed(piles, h)
print(result)
