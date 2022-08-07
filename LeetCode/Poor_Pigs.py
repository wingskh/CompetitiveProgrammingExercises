# https://leetcode.com/problems/poor-pigs/discuss/?currentPage=1&orderBy=hot&query=
import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest/minutesToDie + 1))


buckets = 4
minutesToDie = 15
minutesToTest = 15

sol = Solution()
print(sol.poorPigs(buckets, minutesToDie, minutesToTest))