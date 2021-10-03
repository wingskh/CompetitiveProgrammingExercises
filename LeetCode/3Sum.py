# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r_max = len(nums) - 2
        length_of_nums = len(nums) - 1
        nums.sort()
        result = []

        for i in range(r_max):
            l = i + 1
            r = length_of_nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while r > l:
                diff = nums[l] + nums[r] + nums[i]
                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return result
