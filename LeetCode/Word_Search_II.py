# https://leetcode.com/problems/word-search-ii/
from typing import List
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = None

    def insert(self, word: str) -> None:
        cur_node = self
        for c in word:
            cur_node = cur_node.children[c]
        cur_node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def is_valid_pos(r, c):
            nonlocal r_len, c_len
            return True if 0 <= r < r_len and 0 <= c < c_len else False
        
        def dfs(row, col, trieNode):
            if not is_valid_pos(row, col) or board[row][col] == '.' or board[row][col] not in trieNode.children:
                return 

            c = board[row][col]
            trieNode = trieNode.children[c]
            if trieNode.word is not None:
                result.add(trieNode.word)
            board[row][col] = '.'

            dfs(row+1,col, trieNode)
            dfs(row-1,col, trieNode)
            dfs(row,col+1, trieNode)
            dfs(row,col-1, trieNode)

            board[row][col] = c

        trie = Trie()
        result = set()
        r_len, c_len = len(board), len(board[0])
        for word in words:
            trie.insert(word)

        for r in range(r_len):
            for c in range(c_len):                
                dfs(r, c, trie)
        
        return result
    
    
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = Solution()
result = sol.findWords(board, words)
print(result)
