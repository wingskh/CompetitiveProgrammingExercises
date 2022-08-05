# https://leetcode.com/problems/mirror-reflection/

class Solution:
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)


    def mirrorReflection(self, p: int, q: int) -> int:
        time_for_reflection = self.lcm(p, q)
        is_right_side = True if time_for_reflection/q % 2 == 1 else False
        is_top_side = True if time_for_reflection/p % 2 == 1 else False

        if is_right_side and is_top_side:
            return 1
        elif not is_right_side and is_top_side:
            return 2
            
        return 0


p = 2
q = 1
sol = Solution()
result = sol.mirrorReflection(p, q)
print(result)
