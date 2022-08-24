# https://leetcode.com/problems/poor-pigs/
# https://leetcode.com/problems/poor-pigs/discuss/2387610/Python-oror-Detailed-Explanation-oror-Faster-Than-98-oror-Easily-Understood-oror-Simple-oror-MATH
import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest/minutesToDie + 1))


buckets = 4
minutesToDie = 15
minutesToTest = 15

sol = Solution()
print(sol.poorPigs(buckets, minutesToDie, minutesToTest))