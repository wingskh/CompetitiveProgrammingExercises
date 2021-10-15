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


nums = [10, 9, 2, 5, 3, 7, 101, 18]
sol = Solution()
print(sol.lengthOfLIS(nums))
