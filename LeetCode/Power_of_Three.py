# https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while x <= n:
            if x != n:
                x = x * 3
            else:
                return True
        return False

    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and 1162261467 % n == 0
