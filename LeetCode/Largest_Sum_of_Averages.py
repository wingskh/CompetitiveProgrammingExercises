# https://leetcode.com/problems/largest-sum-of-averages/
class Solution:
    def largestSumOfAverages(self, nums, k):
        def cal_score(i, j):
            nonlocal nums, score_matrix
            if i >= j:
                score_matrix[i][j] = nums[i]
                return nums[i]

            if score_matrix[i][j] is None:
                score_matrix[i][j] = (cal_score(i, j - 1) * (j - i) + nums[j]) / (
                    j - i + 1
                )
            return score_matrix[i][j]

        num_of_nums = len(nums)
        score_matrix = [[None] * num_of_nums for _ in range(num_of_nums)]

        # Initial for the score_matrix
        acc_sum = 0
        for i in range(num_of_nums):
            acc_sum += nums[i]
            score_matrix[0][i] = acc_sum / (i + 1)

        # Initial for the dp
        dp = [[cal_score(0, 0)] + [-1] * (k - 1)] + [
            [cal_score(0, i)] + [-1] * (k - 1) for i in range(1, num_of_nums)
        ]
        # dp[i][j]: max score of partiting the nums[:i+1] into j+1 grps
        # dp[i][j] inferred by min(dp[l][j-1] + score of nums[l+1:]
        # 			   for l in range(i))

        for i in range(num_of_nums):
            for j in range(1, min(k, i + 1)):
                for l in range(i):
                    dp[i][j] = max(dp[l][j - 1] + cal_score(l + 1, i), dp[i][j])

        print(dp)
        return dp[-1][-1]


nums = [9, 1, 2, 3, 9]
k = 3
sol = Solution()
print(sol.largestSumOfAverages(nums, k))
