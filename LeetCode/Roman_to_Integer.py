# https://leetcode.com/problems/roman-to-integer/
# https://leetcode.com/problems/roman-to-integer/discuss/2428756/Python-oror-Easily-Understood-oror-Faster-than-98-oror-Less-than-76-oror-O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))


s = "MCMXCIV"
sol = Solution()
result = sol.romanToInt(s)
print(result)
