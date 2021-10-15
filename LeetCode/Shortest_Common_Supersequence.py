# https://leetcode.com/problems/shortest-common-supersequence/
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length, str2_length = len(str1), len(str2)
        max_length_dp = [list(range(str2_length + 1))] + [
            [i] + [0] * str2_length for i in range(1, str1_length + 1)
        ]

        for i in range(str1_length):
            for j in range(str2_length):
                max_length_dp[i + 1][j + 1] = 1 + (
                    max_length_dp[i][j]
                    if str1[i] == str2[j]
                    else min(max_length_dp[i][j + 1], max_length_dp[i + 1][j])
                )

        i, j = str1_length, str2_length
        result = ""
        while i * j:
            eq_or_use_chr1, eq_or_use_chr2 = (str1[i - 1] == str2[j - 1]), (
                max_length_dp[i - 1][j] < max_length_dp[i][j - 1]
            )
            eq_or_use_chr1, eq_or_use_chr2 = int(eq_or_use_chr1 or eq_or_use_chr2), int(
                eq_or_use_chr1 or not eq_or_use_chr2
            )
            result = (str1[i - 1] if eq_or_use_chr1 else str2[j - 1]) + result
            i -= eq_or_use_chr1
            j -= eq_or_use_chr2

        result = str1[:i] + str2[:j] + result
        return result


str1 = "abac"
str2 = "cab"
sol = Solution()
print(sol.shortestCommonSupersequence(str1, str2))
