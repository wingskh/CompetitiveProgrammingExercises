# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        max_len = 0

        for char in s:
            if char not in current_string:
                current_string += char
            else:
                current_string = current_string[current_string.index(char) + 1 :] + char
            max_len = max(len(current_string), max_len)
        return max_len
