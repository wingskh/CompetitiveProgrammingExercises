# https://leetcode.com/problems/k-diff-pairs-in-an-array/
class Solution:
    def findPairs(self, nums, k) -> int:
        if k == 0:
            k_diff_set = set()
            result = set()
            for i in nums:
                if i not in k_diff_set:
                    k_diff_set.add(i)
                else:
                    result.add(i)
            return len(result)
        else:
            result = 0
            k_diff_set = set(nums)
            for i in k_diff_set:
                if i + k in k_diff_set:
                    result += 1
            return result
