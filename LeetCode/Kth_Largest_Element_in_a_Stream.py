# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
actions = ["KthLargest", "add", "add", "add", "add", "add"]
nums = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# [null, 4, 5, 5, 8, 8]

kthLargest = None
result = [None]
for i in range(len(actions)):
    if actions[i] == 'KthLargest':
        kthLargest = KthLargest(nums[i][0], nums[i][1])
    else:
        result.append(kthLargest.add(nums[i][0]))
print(result)
