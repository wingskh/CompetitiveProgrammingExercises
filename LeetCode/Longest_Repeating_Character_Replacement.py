# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_size = 0
        counter = defaultdict(int)
        left_index = max_length = max_freq = 0

        for right_index in range(len(s)):
            counter[s[right_index]] += 1
            window_size += 1
            max_freq = max(max_freq, counter[s[right_index]])

            while window_size - max_freq > k:
                counter[s[left_index]] -= 1
                left_index += 1
                window_size -= 1

            max_length = max(window_size, max_length)

        return max_length

    
s = "ABAB"
k = 2
s = "AABABBA"
k = 1

sol = Solution()
result = sol.characterReplacement(s, k)
print(result)
