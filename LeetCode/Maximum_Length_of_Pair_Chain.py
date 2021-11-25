# https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort(key=lambda x: x[1])
        cur_tail = -1001
        length = 0
        for elm in pairs:
            if elm[0] > cur_tail:
                cur_tail = elm[1]
                length += 1

        return length


pairs = [
    [1, 9],
    [-6, 10],
    [-5, 8],
    [5, 8],
    [2, 7],
    [-8, -3],
    [2, 6],
    [-4, -2],
    [4, 5],
    [0, 4],
]
sol = Solution()
print(sol.findLongestChain(pairs))
