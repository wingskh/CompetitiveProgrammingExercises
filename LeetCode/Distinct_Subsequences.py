# https://leetcode.com/problems/distinct-subsequences/
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_length = len(s)
        t_length = len(t)
        max_subseq_dp = [[0] * (t_length + 1) for _ in range(s_length + 1)]
        # max_subseq_dp[i][j]:
        # max distinct subsequences for s[:i] and t[:j]

        for i in range(s_length + 1):
            max_subseq_dp[i][0] = 1

        for i in range(s_length):
            for j in range(t_length):
                # If s[i] == t[j], there are 2 types of sequence:
                #   Type 1: subsequences of s[:i-1] and t[:j-1] (just adding s[i] at the last of all sequences)
                #   Type 2: subsequences of s[:i-1] and t[:j] because all type 1 sequences used s[i]
                # If s[i] != t[j], there are 1 types of sequence:
                #   Type 1: subsequences of s[:i-1] and t[:j]
                max_subseq_dp[i + 1][j + 1] = (
                    (max_subseq_dp[i][j] + max_subseq_dp[i][j + 1])
                    if s[i] == t[j]
                    else max_subseq_dp[i][j + 1]
                )

        return max_subseq_dp[-1][-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        print("=============================", 1, len(dp))
        for j in reversed(range(1, len(dp))):
            print(j)

        print(dp)
        for i in range(1, len(s) + 1):
            print(str(s[i - 1]) + " ", end="")
            for j in reversed(range(1, len(dp))):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
            print(dp)
        print(dp)
        return dp[-1]


s = "bagbag"
t = "gag"
sol = Solution()
print(sol.numDistinct(s, t))
