# https://leetcode.com/problems/valid-palindrome/
import re
from turtle import left
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(map(lambda x: x if x.isalnum() else '', s)).lower()
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

s = "ab_a"
sol = Solution()
result = sol.isPalindrome(s)
print(result)



list(str.punctuation)