# https://leetcode.com/problems/longest-palindromic-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_length = len(s)
        # longest_palindromic_subseq_dp[i][j]: longest length of palindromic subseqence for s[i:j+1]
        # MUST initialize with 0 which can confirm that 0 will be returned if i > j
        # We should also initialize the dp[i][j] for i == j to be 1
        longest_palindromic_subseq_dp = [[0] * (s_length) for _ in range(s_length)]

        for subseq_length in range(1, s_length + 1):
            for i in range(s_length - subseq_length + 1):
                j = i + subseq_length - 1
                if j == i:
                    longest_palindromic_subseq_dp[i][j] = 1
                    continue

                if s[i] == s[j]:
                    longest_palindromic_subseq_dp[i][j] = (
                        2 + longest_palindromic_subseq_dp[i + 1][j - 1]
                    )
                else:
                    longest_palindromic_subseq_dp[i][j] = max(
                        longest_palindromic_subseq_dp[i][j - 1],
                        longest_palindromic_subseq_dp[i + 1][j],
                    )

        return longest_palindromic_subseq_dp[0][-1]
