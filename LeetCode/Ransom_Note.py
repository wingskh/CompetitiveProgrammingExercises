# https://leetcode.com/problems/ransom-note/
# https://leetcode.com/problems/ransom-note/discuss/2476142/Python-oror-Easily-Understood-oror-Faster-than-96-oror-Fast
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = Counter(ransomNote)
        magazineDict = Counter(magazine)
        for k in ransomNoteDict:
            magazineDict[k] = magazineDict.get(k, 0) - ransomNoteDict[k]
            if magazineDict[k] < 0:
                return False
        return True


ransomNote = "aa"
magazine = "ab"
sol = Solution()
result = sol.canConstruct(ransomNote, magazine)
print(result)
