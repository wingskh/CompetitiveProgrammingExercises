# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total_number = len(nums)
        dp = [0 for _ in range(total_number)]
        for i in range(1, total_number):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        result = 0
        for num in nums:
            left_index, right_index = 0, result
            while left_index != right_index:
                middle_index = left_index + (right_index - left_index) // 2
                if tails[middle_index] < num:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index
            result = max(result, left_index + 1)
            tails[left_index] = num
        return result


nums = [10, 9, 2, 5, 3, 7, 101, 18]
sol = Solution()
print(sol.lengthOfLIS(nums))
