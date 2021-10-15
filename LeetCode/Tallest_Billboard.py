# https://leetcode.com/problems/tallest-billboard/
class Solution:
    def tallestBillboard(self, rods):
        rod_dp = {0: 0}

        for new_height in rods:
            for diff, acc_height in list(rod_dp.items()):
                rod_dp[diff + new_height] = max(
                    rod_dp.get(diff + new_height, 0), acc_height
                )
                rod_dp[abs(diff - new_height)] = max(
                    rod_dp.get(abs(diff - new_height), 0),
                    acc_height + min(diff, new_height),
                )
        return rod_dp[0]
