# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def binary_search(self, intervals, newInterval):
        left_pointer = 0
        right_pointer = len(intervals) - 1
        while left_pointer < right_pointer:
            middle_index = left_pointer + (right_pointer - left_pointer) // 2
            if newInterval[0] == intervals[middle_index][1]:
                return middle_index
            elif newInterval[0] > intervals[middle_index][1]:
                left_pointer = middle_index + 1
            else:
                right_pointer = middle_index

        return left_pointer

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        index = self.binary_search(intervals, newInterval)
        if newInterval[0] > intervals[index][1]:
            intervals[index], newInterval = newInterval, intervals[index]
        result = intervals[:index] + [newInterval]

        while index < len(intervals) and intervals[index][0] <= result[-1][1]:
            result[-1][0] = min(intervals[index][0], result[-1][0])
            result[-1][1] = max(intervals[index][1], result[-1][1])
            index += 1

        return result + intervals[index:]


# [[1,2],[3,10],[12,16]]

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
# Output: [[1,5],[6,9]]

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8]
# Output: [[1,2],[3,10],[12,16]]

# intervals = [[1, 5]]
# newInterval = [2, 3]
# Output: [[1,5]]

intervals = [[1, 5]]
newInterval = [6, 8]
# Output: [[1,5],[6,8]]

sol = Solution()
result = sol.insert(intervals, newInterval)
print(result)
