# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            distance = -math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            if len(heap) < k:
                heapq.heappush(heap, (distance, point))
            elif distance > heap[0][0]:
                heapq.heapreplace(heap, (distance, point))

        return [x[1] for x in heap]
    

points = [[1,3],[-2,2]]
k = 1
# Output: [[-2,2]]
points = [[3,3],[5,-1],[-2,4]]
k = 2
# Output: [[3,3],[-2,4]]
sol = Solution()
result = sol.kClosest(points, k)
print(result)
