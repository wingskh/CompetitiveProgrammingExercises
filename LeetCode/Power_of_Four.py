# https://leetcode.com/problems/power-of-four/
# https://leetcode.com/problems/power-of-four/discuss/2461447/python-easily-understood-faster-than-92-explanation

class Solution:
    def isPowerOfFour2(self, n: int) -> bool:
        bin_num = bin(n)
        zero_count = bin_num.count('0')
        return zero_count % 2 == 1 and bin_num[2] == '1' and zero_count + 2 == len(bin_num)

n = 17
sol = Solution()
print(sol.isPowerOfFour(n))