# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
from collections import defaultdict

class Solution:
    # Using 2 pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while numbers[left_index] + numbers[right_index] != target:
            print(left_index, right_index, numbers[left_index], numbers[right_index])
            if numbers[left_index] + numbers[right_index] > target:
                right_index -= 1
            elif numbers[left_index] + numbers[right_index] < target:
                left_index += 1

        return [left_index+1, right_index+1]
    
    # Using Dict
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_finder = defaultdict(int)
        nums_len = len(numbers)

        for i in range(nums_len):
            if target - numbers[i] in index_finder:
                return [index_finder[target - numbers[i]] + 1, i + 1]
            index_finder[numbers[i]] = i


numbers = [5,25,75]
target = 100
sol = Solution()
print(sol.twoSum(numbers, target))
