# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums, target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
            if nums[middle_pointer] == target:
                return middle_pointer

            if nums[left_pointer] <= nums[middle_pointer]:
                if nums[left_pointer] <= target < nums[middle_pointer]:
                    right_pointer = middle_pointer - 1
                else:
                    left_pointer = middle_pointer + 1
            else:
                if nums[middle_pointer] < target <= nums[right_pointer]:
                    left_pointer = middle_pointer + 1
                else:
                    right_pointer = middle_pointer - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
sol = Solution()
result = sol.search(nums, target)
print(result)
