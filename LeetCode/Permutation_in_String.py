# https://leetcode.com/problems/permutation-in-string/
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_all_zero():
            for key in counter:
                if counter[key] != 0:
                    return False
            return True
        
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        
        counter = defaultdict(int)

        for i in range(s1_len):
            counter[s1[i]] -= 1
            counter[s2[i]] += 1

        if is_all_zero(): return True

        for i in range(s1_len, s2_len):
            counter[s2[i]] += 1
            counter[s2[i - s1_len]] -= 1
            if is_all_zero(): return True

        return False


s1 = "ab"
s2 = "eidbaooo"
sol = Solution()
result = sol.checkInclusion(s1, s2)
print(result)
