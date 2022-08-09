# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))