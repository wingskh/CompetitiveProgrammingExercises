# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindromic = ""
        max_len = 0
        max_right_index = len(s)
        for index in range(len(s)):
            # Detect palindromic with odd length
            left_index, right_index = index, index
            while (
                left_index >= 0
                and right_index < max_right_index
                and s[left_index] == s[right_index]
            ):
                if right_index - left_index + 1 >= max_len:
                    longest_palindromic = s[left_index : right_index + 1]
                    max_len = right_index - left_index + 1
                left_index -= 1
                right_index += 1

            # Detect palindromic with even length
            left_index, right_index = index, index + 1
            while (
                left_index >= 0
                and right_index < max_right_index
                and s[left_index] == s[right_index]
            ):
                if right_index - left_index + 1 >= max_len:
                    longest_palindromic = s[left_index : right_index + 1]
                    max_len = right_index - left_index + 1
                left_index -= 1
                right_index += 1

        return longest_palindromic
