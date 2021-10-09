# https://leetcode.com/problems/burst-balloons/
class Solution:
    def maxCoins(self, nums):
        nums_length = len(nums)
        max_coins_dp = [[0] * nums_length for _ in range(nums_length)]

        # Length of the subarray
        for length in range(1, nums_length + 1):
            # Starting index
            for i in range(nums_length - length + 1):
                # Ending index
                j = i + length - 1
                max_coins_dp[i][j] = -1
                left_num = 1 if i == 0 else nums[i - 1]
                right_num = 1 if j == nums_length - 1 else nums[j + 1]
                # The last ballon that will be bursted
                for k in range(i, j + 1):
                    prev_score = max_coins_dp[i][k - 1] if k != 0 else 0
                    prev_score += max_coins_dp[k + 1][j] if k != nums_length - 1 else 0
                    max_coins_dp[i][j] = max(
                        prev_score + left_num * nums[k] * right_num,
                        max_coins_dp[i][j],
                    )

        return max_coins_dp[0][-1]
