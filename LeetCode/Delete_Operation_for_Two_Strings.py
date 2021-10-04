# https://leetcode.com/problems/delete-operation-for-two-strings/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length = len(word1)
        word2_length = len(word2)

        min_distance_dp = [[i for i in range(word2_length+1)]] + [[i] + [math.inf] * (word2_length) for i in range(1, word1_length+1)]

        for i in range(word1_length):
            for j in range(word2_length):
                min_distance_dp[i + 1][j + 1] = min_distance_dp[i][j] if word1[i] == word2[j] else min(min_distance_dp[i+1][j], min_distance_dp[i][j+1]) + 1

        return min_distance_dp[-1][-1]
