# https://leetcode.com/problems/last-stone-weight-ii/
class Solution:
    # Dynamic Programming
    def lastStoneWeightII(self, stones) -> int:
        stones_length = len(stones)
        total_weight = sum(stones)
        possible_range = total_weight * 2 + 1

        weight_diff_dp = [[0] * possible_range for _ in range(stones_length)]
        weight_diff_dp[0][total_weight - stones[0]] = 1
        weight_diff_dp[0][total_weight + stones[0]] = 1

        for i in range(1, stones_length):
            for s in range(possible_range):
                # left side
                if s - stones[i] >= 0 and weight_diff_dp[i - 1][s - stones[i]] > 0:
                    weight_diff_dp[i][s] += weight_diff_dp[i - 1][s - stones[i]]
                # right operation
                if (
                    s + stones[i] <= possible_range - 1
                    and weight_diff_dp[i - 1][s + stones[i]] > 0
                ):
                    weight_diff_dp[i][s] += weight_diff_dp[i - 1][s + stones[i]]

        for i in range(total_weight, possible_range):
            if weight_diff_dp[-1][i] != 0:
                return i - total_weight

        return -1

    # Find all combination using set
    def lastStoneWeightII(self, stones):
        stones_length = len(stones)
        last_round_comb = set()
        last_round_comb.add(stones[0])

        for i in range(1, stones_length):
            cur_round_comb = set()
            for s in last_round_comb:
                cur_round_comb.add(abs(s - stones[i]))
                cur_round_comb.add(s + stones[i])
            last_round_comb = cur_round_comb

        return min(last_round_comb)
