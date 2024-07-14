# https://leetcode.com/problems/non-overlapping-intervals
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if there are many duplicated intervals, we can use a set to remove them
        # nonduplicate_intervals = {tuple(interval) for interval in intervals}
        # counter = len(intervals) - len(nonduplicate_intervals)
        # intervals = list(nonduplicate_intervals)

        intervals.sort(key=lambda x: x[1])
        counter = 0
        last_index = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last_index][1]:
                counter += 1
            else:
                last_index = i
        return counter

# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# Output: 1

intervals = [[1, 2], [1, 2], [1, 2]]
# Output: 2

intervals = [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]
# Output: 4

intervals = [
    [-52, 31],
    [-73, -26],
    [82, 97],
    [-65, -11],
    [-62, -49],
    [95, 99],
    [58, 95],
    [-31, 49],
    [66, 98],
    [-63, 2],
    [30, 47],
    [-40, -26],
]
# Output: 7

intervals = [[-39,21],[-38,5],[-67,67],[23,37],[83,95],[-71,-19],[-19,64],[4,31],[37,96],[30,57],[-19,12],[53,75],[-54,83],[-32,38],[-18,16],[-60,9],[92,93],[-12,20],[-37,35],[19,36],[46,56],[45,52],[-67,-29],[30,67],[67,79],[52,98],[59,60],[-63,7],[7,20],[16,59],[83,96],[-59,-3],[33,41],[-67,-49],[-15,67]]
# Output: 27

sol = Solution()
result = sol.eraseOverlapIntervals(intervals)
print(result)
