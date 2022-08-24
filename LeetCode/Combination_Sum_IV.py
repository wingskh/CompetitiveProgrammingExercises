# https://leetcode.com/problems/combination-sum-iv/
# https://leetcode.com/problems/combination-sum-iv/discuss/2381090/python-easily-understood-dp-faster-than-92-simple

class Solution:
    # # If target is small
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     dp = [0] * (target+1)
    #     dp[0] = 1
    #     for i in range(1, target+1):
    #         for num in nums: 
    #             before_num = i - num
    #             if before_num >= 0:
    #                 print(i, num)
    #                 dp[i] += dp[before_num]

    #     return dp[target]

    def combinationSum5(self, nums, target: int) -> int:
        dp = {}
        dp[0] = [1]

        def search(target):
            if target in dp:
                return dp[target]
            comb_sum = 0
            for num in nums:
                if target > num:
                    comb_sum += search(target - num)
                elif target == num:
                    comb_sum += 1
            dp[target] = comb_sum
            return comb_sum

        return search(target)


nums = [4,2,1]
target = 32
sol = Solution()
print(sol.combinationSum4(nums, target))
print(sol.combinationSum5(nums, target))