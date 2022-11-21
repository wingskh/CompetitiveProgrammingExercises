# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left_index, right_index = 0, len(nums) - 1
    #     while left_index <= right_index:
    #         mid_index = left_index + (right_index - left_index) // 2

    #         if target == nums[mid_index]:
    #             return mid_index
    #         elif target < nums[mid_index]:
    #             right_index = mid_index - 1
    #         else:
    #             left_index = mid_index + 1
        
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        left_index, right_index = 0, len(nums) - 1
        while left_index < right_index:
            mid_index = left_index + (right_index - left_index) // 2
            if target < nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index 
                
        return -1 if nums[left_index] != target else left_index

nums = [2,5]
target = 5
sol = Solution()
result = sol.search(nums, target)
print(result)
