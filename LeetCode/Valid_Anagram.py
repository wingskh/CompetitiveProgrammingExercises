# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_str_dict = dict()
        second_str_dict = dict()
        
        for i in s:
            if i not in first_str_dict:
                first_str_dict[i] = 1
            else:
                first_str_dict[i] += 1
                
        for i in t:
            if i not in second_str_dict:
                second_str_dict[i] = 1
            else:
                second_str_dict[i] += 1
                
        return first_str_dict == second_str_dict


s = "anagram"
t = "nagaram"
sol = Solution()
result = sol.isAnagram(s, t)
print(result)
