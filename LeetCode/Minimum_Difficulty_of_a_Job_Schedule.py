# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/submissions/
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        # Calculate the difficulty for a day with
        # daily_difficulty_dp [i:j+1]
        # Assume that i <= j
        def cal_difficulty_for_a_day(i, j):
            nonlocal daily_difficulty_dp, jobDifficulty

            if i == j:
                daily_difficulty_dp[i][j] = jobDifficulty[i]
            elif daily_difficulty_dp[i][j] is None:
                daily_difficulty_dp[i][j] = max(
                    cal_difficulty_for_a_day(i, j - 1), jobDifficulty[j]
                )
            return daily_difficulty_dp[i][j]

        job_difficulty_length = len(jobDifficulty)
        if job_difficulty_length < d:
            return -1
        elif job_difficulty_length == d:
            return sum(jobDifficulty)

        daily_difficulty_dp = [
            [None] * job_difficulty_length for _ in range(job_difficulty_length)
        ]

        for i in range(job_difficulty_length):
            daily_difficulty_dp[i][i] = jobDifficulty[i]

        max_jd = 1000 * 300
        min_job_diff_dp = [[max_jd] * (d) for _ in range(job_difficulty_length)]
        min_job_diff_dp[0][0] = jobDifficulty[0]
        for i in range(1, job_difficulty_length):
            min_job_diff_dp[i][0] = max(min_job_diff_dp[i - 1][0], jobDifficulty[i])

        for i in range(job_difficulty_length):
            for j in range(1, min(i + 1, d)):
                for k in range(i):
                    min_job_diff_dp[i][j] = min(
                        min_job_diff_dp[k][j - 1] + cal_difficulty_for_a_day(k + 1, i),
                        min_job_diff_dp[i][j],
                    )

        return min_job_diff_dp[-1][-1]
