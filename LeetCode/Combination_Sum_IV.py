# https://leetcode.com/problems/combination-sum-iv/

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
        
        if not nums or target <= 0:
            return 0

        ans = 0
        memo = dict()
        def bt(rem):
            if rem == 0:
                return 1
            if rem in memo:
                return memo[rem]
            count = 0
            for num in nums:
                if num <= rem:
                    this_count = bt(rem-num)
                    count += this_count
            memo[rem] = count
            return count
        
        return bt(target)

        def combinationSum4(self, nums, target):
            dp = {}
            dp[0] = [1]

            def search(target):
                if target < 0:
                    return 0
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