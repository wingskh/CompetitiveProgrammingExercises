# https://leetcode.com/problems/split-array-into-consecutive-subsubsequenceuences/
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/2448243/python-easily-understood-faster-than-90-explanation
from collections import Counter
from collections import defaultdict

class Solution:
    def isPossible(self, nums: int) -> bool:
        subsequence = defaultdict(int)
        num_count = Counter(nums)
        
        for num in nums:
            if not num_count[num]:
                continue

            if subsequence[num - 1] > 0:
                subsequence[num - 1] -= 1
                subsequence[num] += 1
            else:
                if not num_count[num + 1] or not num_count[num + 2]:
                    return False
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1
                subsequence[num + 2] += 1
            num_count[num] -= 1

        return True


nums = [1,2,3,3,4,4,5,5]
sol = Solution()
print(sol.isPossible(nums))
