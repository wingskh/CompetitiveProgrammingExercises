# https://leetcode.com/problems/binary-trees-with-factors/
import math

class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        total_nums = len(arr)
        moduler = 1000000007
        count_product_dict = {num: 1 for num in arr}
        arr.sort()

        for i in range(1, total_nums):
            for j in range(i):
                quotient = arr[i] // arr[j]
                if quotient < 2 or math.sqrt(arr[i]) > arr[i- 1]:
                    break
                if arr[i] % arr[j] == 0 and quotient in count_product_dict:
                    count_product_dict[arr[i]] += count_product_dict[arr[j]] * count_product_dict.get(quotient, 0)
                    count_product_dict[arr[i]] %= moduler
                    
        return sum(count_product_dict.values()) % moduler


    def numFactoredBinaryTrees2(self, arr) -> int:
        arr.sort()
        MOD = 10**9 + 7
        
        # create a dictionary and initialize
        dp = {}
        for n in arr:
            dp[n] = 1
            
        # loop through each number
        for i, n in enumerate(arr):
            for j in range(i):
                if not(n % arr[j]) and n // arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n//arr[j]]
                    dp[n] %= MOD
        
        print(dp)
        return sum(dp.values()) % MOD


# [2,4,5,10]
# [ ,4,5,10]
arr = [2,4]
arr = [18,3,6,2]
# arr = [45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
sol = Solution()
result = sol.numFactoredBinaryTrees(arr)
print(result)
result = sol.numFactoredBinaryTrees2(arr)
print(result)
        