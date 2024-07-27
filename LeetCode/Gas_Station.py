# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        print("*" * 100)
        net_gas = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(net_gas) < 0:
            return -1
        acc_gas = start_point = 0

        for i in range(len(gas)):
            acc_gas += net_gas[i]
            if acc_gas < 0:
                start_point = i + 1
                acc_gas = 0

        return start_point


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
# Output = 3
# gas = [2, 3, 4]
# cost = [3, 4, 3]
# Output = -1
# gas = [5, 8, 2, 8]
# cost = [6, 5, 6, 6]
# Output = 3
# gas = [2, 3, 4]
# cost = [3, 4, 3]
# Output = -1
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
