# https://leetcode.com/problems/sliding-window-maximum/
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        queue = deque()
        left = right = 0
        nums_len = len(nums)

        while right < nums_len:
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()
                
            if right + 1 >= k:
                max_list.append(nums[queue[0]])
                left += 1
            right += 1
        
        return max_list


nums = [1,3,-1,-3,5,3,6,7]
k = 3
# [3,3,5,5,6,7]

sol = Solution()
result = sol.maxSlidingWindow(nums, k)
print(result)
