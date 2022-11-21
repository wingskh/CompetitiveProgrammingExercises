# https://leetcode.com/problems/insert-interval/
from re import L
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_index, right_index = 0, len(intervals) - 1

        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if newInterval[0] == intervals[middle_index][0]:
                left_index = middle_index
                break
            if newInterval[0] < intervals[middle_index][0]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        intervals.insert(left_index, newInterval)
        prev_index = max(left_index-1, 0)
        cur_index = prev_index + 1

        started = False
        while cur_index < len(intervals):
            if intervals[prev_index][1] >= intervals[cur_index][0]:
                started = True
                intervals[prev_index][1] = max(intervals[prev_index][1], intervals[cur_index][1])
                intervals.pop(cur_index)
            else:
                if started:
                    break
                cur_index += 1
                prev_index += 1
        return intervals

# [[1,2],[3,10],[12,16]]

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# x < nums[start][1] 
# y <= nums[end][0]
intervals = [[2, 5], [6, 7], [8, 9]]
newInterval = [0, 1]
sol = Solution()
result = sol.insert(intervals, newInterval)
print(result)



# def insert(self, intervals, newInterval):
#     left_pointer = 0
#     right_pointer = len(intervals) - 1

#     while left_pointer < right_pointer:
#         middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
#         if intervals[middle_pointer][1] < newInterval[0]:
#             left_pointer = middle_pointer + 1
#         else:
#             right_pointer = middle_pointer

#     start_index = left_pointer
#     right_pointer = len(intervals) - 1

#     while left_pointer < right_pointer:
#         middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
#         if intervals[middle_pointer][0] <= newInterval[1]:
#             left_pointer = middle_pointer + 1
#         else:
#             right_pointer = middle_pointer

#     end_index = left_pointer
#     print(start_index, end_index)
#     if start_index == end_index:
#         if start_index == len(intervals) - 1:
#             if intervals[start_index][1] >= newInterval[0]:
#                 intervals[start_index][1] = max(intervals[start_index][1], newInterval[1])
#             else:
#                 intervals.append(newInterval)
#         else:
#             intervals.insert(start_index, newInterval)
#         return intervals
#     else:
#         start_index -= 1
        
#     if intervals[start_index][1] >= newInterval[0]:
#         print("="*50, 2)
#         newInterval[0] = intervals[start_index][0]
#     else:
#         start_index += 1

#     newInterval[1] = max(intervals[end_index-1][1], newInterval[1])
#     print(intervals[:start_index] )
#     return intervals[:start_index] + [newInterval] + intervals[end_index:]


# def insert2(self, intervals, newInterval):
#     def leftmost_binary_search(mode, target, left_pointer=0):
#         right_pointer = len(intervals) - 1

#         while left_pointer < right_pointer:
#             middle_pointer = left_pointer + (left_pointer + right_pointer) // 2
#             print("middle_pointer:", middle_pointer, left_pointer, right_pointer)
#             if intervals[middle_pointer][mode] <= target:
#                 left_pointer = middle_pointer + 1
#             else:
#                 right_pointer = middle_pointer

#         return left_pointer

#     start_index = leftmost_binary_search(1, newInterval[0])
#     print("=" * 50)
#     end_index = leftmost_binary_search(0, newInterval[1], left_pointer=start_index)

#     print(start_index, end_index)
#     return []

