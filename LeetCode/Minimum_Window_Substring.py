# https://leetcode.com/problems/minimum-window-substring/
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_all_less_than_zero():
            for key in counter:
                if counter[key] > 0:
                    return False
            return True

        counter = Counter(t)
        min_mindow_str = ""
        left_index = right_index = 0
        
        for right_index in range(len(s)):
            if s[right_index] in counter:
                counter[s[right_index]] -= 1
                
            if is_all_less_than_zero():
                while s[left_index] not in counter or counter[s[left_index]] < 0:
                    if s[left_index] in counter:
                        counter[s[left_index]] += 1
                    left_index += 1

                if len(min_mindow_str) == 0 or len(min_mindow_str) > len(s[left_index:right_index + 1]):
                    min_mindow_str = s[left_index:right_index + 1]
                
                counter[s[left_index]] += 1
                left_index += 1
        
        return min_mindow_str


s = "ADOBECODEBANC"
t = "ABC"
# "BANC"
sol = Solution()
result = sol.minWindow(s, t)
print(result)
