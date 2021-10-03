# https://leetcode.com/problems/interleaving-string/
class Solution:
    # Recursion
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache  # memorize the past recursion result (>=python 3.9)
        def dfs(s1_index, s2_index, target_index):
            nonlocal s1_length, s2_length, s3_length
            if target_index == s3_length:
                return True

            result = False
            if s1_index < s1_length and s1[s1_index] == s3[target_index]:
                result |= dfs(s1_index + 1, s2_index, target_index + 1)
            if s2_index < s2_length and s2[s2_index] == s3[target_index]:
                result |= dfs(s1_index, s2_index + 1, target_index + 1)

            return result

        s1_length, s2_length, s3_length = len(s1), len(s2), len(s3)
        return dfs(0, 0, 0) if s1_length + s2_length == s3_length else False

    # Dynamic Programming
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_length, s2_length, s3_length = len(s1), len(s2), len(s3)
        if s1_length + s2_length != s3_length:
            return False

        interleaving_dp = [[False] * (s2_length + 1) for _ in range(s1_length + 1)]
        # Initialize the dp matrix
        interleaving_dp[0][0] = True
        for i in range(1, s1_length + 1):
            interleaving_dp[i][0] = interleaving_dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, s2_length + 1):
            interleaving_dp[0][j] = interleaving_dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(s1_length):
            for j in range(s2_length):
                if s1[i] == s3[i + j + 1] and interleaving_dp[i][j + 1]:
                    interleaving_dp[i + 1][j + 1] = True
                elif s2[j] == s3[i + j + 1] and interleaving_dp[i + 1][j]:
                    interleaving_dp[i + 1][j + 1] = True

        return interleaving_dp[-1][-1]
