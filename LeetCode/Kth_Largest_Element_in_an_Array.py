# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
                
        return heap[0]

    

# nums = [3,2,1,5,6,4]
# k = 2
# Output: 5
# nums = [1]
# k = 1
# Output: 1
nums = [3,2,3,1,2,4,5,5,6]
k = 4
# Output: 4
sol = Solution()
result = sol.findKthLargest(nums, k)
print(result)
