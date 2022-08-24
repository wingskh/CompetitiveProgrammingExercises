# https://leetcode.com/problems/first-unique-character-in-a-string/
# https://leetcode.com/problems/first-unique-character-in-a-string/discuss/2431833/python-easily-understood-faster-than-997-5-lines

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chr_count = Counter(s)

        for x in chr_count:
            if chr_count[x] == 1:
                return s.index(x)
        return -1