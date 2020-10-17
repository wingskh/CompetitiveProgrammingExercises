# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3498/
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) <= 10:
            return result
        unique_set = set()
        for i in range(len(s)-9):
            sub_string = s[i:i+10]
            if sub_string not in unique_set:
                unique_set.add(sub_string)
            else:
                if sub_string not in result:
                    result.append(sub_string)
        return result


sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
