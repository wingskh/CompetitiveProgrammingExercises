# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from typing import Optional

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.is_end_of_word = True

    
    def search(self, word: str) -> bool:
        def find(cur_node: TrieNode, index: int) -> Optional[TrieNode]:
                if index == len(word):
                    return cur_node.is_end_of_word
                chr = word[index]
            
                if chr == '.':
                    for c in cur_node.children:
                        if find(cur_node.children[c], index + 1):
                            return True
                else:
                    if chr not in cur_node.children:
                        return False
                    return find(cur_node.children[chr], index + 1)

        return find(self.root, 0)
    
    
result = [None]
wordDictionary = WordDictionary()
actions = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
values = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
actions = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
values = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

actions = ["WordDictionary","addWord","search"]
values = [[],["bad"],["b.."]]

# actions = ["WordDictionary","addWord","addWord","search"]
# values = [[],["a"],["a"],["."]]

for i in range(1, len(actions)):
    if actions[i] == 'addWord':
        result.append(wordDictionary.addWord(values[i][0]))
    elif actions[i] == 'search':
        result.append(wordDictionary.search(values[i][0]))

print(result)

 