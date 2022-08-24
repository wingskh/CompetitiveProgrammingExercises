# https://leetcode.com/problems/contains-duplicate/
# https://leetcode.com/problems/contains-duplicate/discuss/2381975/python-easily-understood-dp-faster-than-88-simple


class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))