# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        acc = 1
        nums_len = len(nums)
        
        for num in nums:
            result.append(acc)
            acc *= num

        acc = 1
        for i in range(nums_len - 1, -1, -1):
            result[i] *= acc
            acc *= nums[i]

        return result

nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))
