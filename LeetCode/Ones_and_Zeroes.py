# https://leetcode.com/problems/ones-and-zeroes/
class Solution:
    # Dynamic Programming
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs_len = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(strs_len)]
        zeros_count = strs[0].count("0")
        ones_count = len(strs[0]) - zeros_count
        if zeros_count <= m and ones_count <= n:
            dp[0][zeros_count][ones_count] = 1

        for i in range(1, strs_len):
            zeros_count = strs[i].count("0")
            ones_count = len(strs[i]) - zeros_count
            for a in range(m + 1):
                for b in range(n + 1):
                    if a - zeros_count >= 0 and b - ones_count >= 0:
                        dp[i][a][b] = max(
                            dp[i][a][b],
                            dp[i - 1][a - zeros_count][b - ones_count] + 1,
                            dp[i - 1][a][b],
                        )
                    else:
                        dp[i][a][b] = max(dp[i][a][b], dp[i - 1][a][b])

        return max(map(max, dp[-1]))

    # Find all combination using set
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs_len = len(strs)
        last_round_comb = set()
        for i in range(strs_len):
            zeros_count = strs[i].count("0")
            ones_count = len(strs[i]) - zeros_count
            cur_round_comb = set()
            if zeros_count <= m and ones_count <= n:
                cur_round_comb.add((zeros_count, ones_count, 1))

            for acc_zero, acc_one, subset_size in last_round_comb:
                added_zeros = zeros_count + acc_zero
                added_ones = ones_count + acc_one

                if added_zeros <= m and added_ones <= n:
                    cur_round_comb.add((added_zeros, added_ones, subset_size + 1))

            last_round_comb = set.union(last_round_comb, cur_round_comb)

        return (
            max([subset_size for _, _, subset_size in last_round_comb])
            if last_round_comb
            else 0
        )
