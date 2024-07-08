# https://leetcode.com/problems/minimum-interval-to-include-each-query/
from collections import deque
from typing import List
from heapq import heappush, heappop


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = deque(sorted(intervals, key=lambda x: x[0]))
        prev_intervals_heap = []
        min_interval_map = {}
        for query in sorted(set(queries)):
            while intervals and intervals[0][0] <= query:
                start, end = intervals.popleft()
                heappush(prev_intervals_heap, (end-start+1, end))
            
            while prev_intervals_heap and prev_intervals_heap[0][1] < query:
                heappop(prev_intervals_heap)
            
            min_interval_map[query] = prev_intervals_heap[0][0] if prev_intervals_heap else -1

        return [min_interval_map[query] for query in queries]


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
# Output: [3,3,1,4]

intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries = [2, 19, 5, 22]
# Output: [2,-1,4,6]


sol = Solution()
print(sol.minInterval(intervals, queries))
