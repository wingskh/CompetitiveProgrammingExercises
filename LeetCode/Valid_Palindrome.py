# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(map(lambda x: x.lower() if x.isalnum() else '', s))
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True

s = "ab_a"
sol = Solution()
result = sol.isPalindrome(s)
print(result)

