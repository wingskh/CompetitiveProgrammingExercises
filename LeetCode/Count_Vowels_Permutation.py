# https://leetcode.com/problems/count-vowels-permutation/
# https://leetcode.com/problems/count-vowels-permutation/discuss/2391936/Python-oror-Detailed-Explanation-oror-Easily-Understood-oror-DP-oror-Simple-oror-MATH

import math

class Solution:
    # Reduced Space Complexity
    def countVowelPermutation(self, n: int) -> int:
        moduler = math.pow(10, 9) + 7
        a, e, i, o, u = [1] * 5
        for _ in range(n - 1):
            a, e, i, o, u = map(lambda x: x % moduler, [(e + i + u), (a + i), (e + o), (i), (i + o)])
        return int((a + e + i+ o + u) % moduler)

    # Easy Understood
    def countVowelPermutation2(self, n: int) -> int:
        # dp[i][j] means the number of strings of length i that ends with the j-th vowel.
        dp = [[1] * 5] + [[0] * (5) for _ in range(n - 1)]
        moduler = math.pow(10, 9) + 7
        for i in range(1, n):
            # For vowel a
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % moduler
            # For vowel e
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % moduler
            # For vowel i
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % moduler
            # For vowel o
            dp[i][3] = (dp[i - 1][2]) % moduler
            # For vowel u
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % moduler
            
        return int(sum(dp[-1]) % moduler)

n = 2 # 
sol = Solution()
result = sol.countVowelPermutation(n)
print(result)
result = sol.countVowelPermutation2(n)
print(result)