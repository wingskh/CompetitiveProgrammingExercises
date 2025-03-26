# https://leetcode.com/problems/word-ladder/

from typing import List
from collections import deque


class Solution:
    def is_one_letter_difference(self, word1: str, word2: str) -> bool:
        return sum(1 for a, b in zip(word1, word2) if a != b) == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        queue = deque([(beginWord, 1)])
        seen = set([beginWord])
        while queue:
            current_word, current_length = queue.popleft()
            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = current_word[:i] + c + current_word[i + 1 :]
                    if new_word in word_set and new_word not in seen:
                        if new_word == endWord:
                            return current_length + 1
                        seen.add(new_word)
                        queue.append((new_word, current_length + 1))

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# Output: 5
beginWord = "hit"
endWord = "aaa"
wordList = ["hot", "ait", "dot", "dog", "aat", "lot", "cot", "aaa"]
# Output: 4
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))
