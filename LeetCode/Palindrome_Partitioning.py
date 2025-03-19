# https://leetcode.com/problems/palindrome-partitioning/
from typing import List

class Solution:
    def __init__(self):
        self.result = [] 

    def is_palindroome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        stack = []
        ans = []
        s_len = len(s)
        def dfs(index):
            if index == s_len:
                for partition in stack:
                    if not self.is_palindroome(partition):
                        return

                ans.append(stack.copy())
                return

            if stack:
                stack[-1] += s[index]
                dfs(index + 1)
                stack[-1] = stack[-1][:-1]
            
            stack.append(s[index])
            dfs(index + 1)
            stack.pop()

        dfs(0)
        return ans


s = "aab"
# Output = [["a","a","b"],["aa","b"]]
sol = Solution()
print(sol.partition(s))
