# https://leetcode.com/problems/word-ladder-ii/
from collections import defaultdict

class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i]+"*"+word[i+1:]].append(word)
        print(d)

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
result = sol.findLadders(beginWord, endWord, wordList)
print(result)
