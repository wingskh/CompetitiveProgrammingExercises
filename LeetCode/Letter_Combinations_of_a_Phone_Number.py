# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        total_digit = len(digits)
        if total_digit < 1:
            return []

        def backtracking(str, index):
            nonlocal result, total_digit
            if len(str) == total_digit:
                result.append(str)
                return

            for s in letters[digits[index]]:
                backtracking(str + s, index + 1)

        backtracking("", 0)
        return result
