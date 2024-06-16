# https://leetcode.com/problems/find-median-from-data-stream/
import heapq


class MedianFinder:
    def __init__(self):
        self.left_half = []
        self.right_half = []
        heapq.heapify(self.left_half)
        heapq.heapify(self.right_half)

    def addNum(self, num: int) -> None:
        if len(self.right_half) == 0 or num >= self.right_half[0]:
            heapq.heappush(self.right_half, num)
        else:
            heapq.heappush(self.left_half, -num)
        
        if len(self.right_half) < len(self.left_half):
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        elif len(self.right_half) > len(self.left_half) + 1:
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def findMedian(self) -> float:
        return (-self.left_half[0] + self.right_half[0]) / 2 if len(self.left_half) == len(self.right_half) else self.right_half[0]

    
medianFinder = MedianFinder()
medianFinder.addNum(1)
# arr = [1]
medianFinder.addNum(2)
# arr = [1, 2]
print(medianFinder.findMedian())
# return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)
# arr[1, 2, 3]
print(medianFinder.findMedian())
# return 2.0
