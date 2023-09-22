# https://leetcode.com/problems/implement-trie-prefix-tree/
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.is_end_of_word = True

    def find_last(self, word: str) -> Optional[TrieNode]:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                return None
            cur_node = cur_node.children[c]
        return cur_node

    def search(self, word: str) -> bool:
        last_node = self.find_last(word)
        return False if last_node is None else last_node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        last_node = self.find_last(prefix)
        return False if last_node is None else True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
result = [None]
trie = Trie()
result.append(trie.insert("apple"))
result.append(trie.search("apple"))   # return True
result.append(trie.search("app"))     # return False
result.append(trie.startsWith("app")) # return True
result.append(trie.insert("app"))
result.append(trie.search("app"))     # return True
print(result)
