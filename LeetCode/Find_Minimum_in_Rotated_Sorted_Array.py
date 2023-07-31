# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        elif nums[-1] < nums[-2]:
            return nums[-1]
        
        left_index, right_index = 0, len(nums) - 1
        
        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if nums[middle_index] < nums[middle_index - 1]:
                left_index = middle_index 
                break
            if nums[middle_index] >= nums[left_index]:
                left_index = middle_index
            else:
                right_index = middle_index

        return nums[left_index]
    

# nums = [3,4,5,1,2]
# nums = [[11,13,15,17]]
nums = [4,5,6,7,0,1,2]
# nums = [5,6,7,0,1,2,4]
# nums = [2,1]
sol = Solution()
result = sol.findMin(nums)
print(result)
