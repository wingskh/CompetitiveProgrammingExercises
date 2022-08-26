# https://leetcode.com/problems/reordered-power-of-2/
# https://leetcode.com/problems/reordered-power-of-2/discuss/2482894/Python-oror-Easily-Understood-oror-Faster-than-96-oror-Fast
from functools import lru_cache

@lru_cache
def get_all_power_of_2():
    return [sorted(str(1 << i)) for i in range(30)] 

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in get_all_power_of_2()


n = 125
sol = Solution()
result = sol.reorderedPowerOf2(n)
print(result)