# https://leetcode.com/problems/poor-pigs/
# https://leetcode.com/problems/poor-pigs/discuss/2387610/Python-oror-Detailed-Explanation-oror-Faster-Than-98-oror-Easily-Understood-oror-Simple-oror-MATH
import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(round(math.log(buckets, minutesToTest // minutesToDie + 1), 10))

buckets = 125
minutesToDie = 1
minutesToTest = 4
# Output = 3

# buckets = 4
# minutesToDie = 15
# minutesToTest = 30
# # Output = 2

# buckets = 90
# minutesToDie = 2
# minutesToTest = 7
# Output = 4

sol = Solution()
print(sol.poorPigs(buckets, minutesToDie, minutesToTest))
