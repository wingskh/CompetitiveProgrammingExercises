# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_num = dict()
        for index, num in enumerate(nums):
            if target - num in last_num:
                return [last_num[target - num], index]
            else:
                last_num[num] = index

nums = [3,2,4]
target = 6
sol = Solution()
result = sol.twoSum(nums, target)
print(result)
