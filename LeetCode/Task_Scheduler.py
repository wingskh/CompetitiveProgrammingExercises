# https://leetcode.com/problems/task-scheduler/
import heapq
from typing import List
from collections import defaultdict
from collections import deque
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        freq_counter = Counter(tasks)
        heap = [-x for x in freq_counter.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while queue or heap:
            time += 1
            if heap:
                new_count = heapq.heappop(heap) + 1
                if new_count:
                    queue.append([time + n, new_count])
            
            if queue and queue[0][0] == time:
                heapq.heappush(heap, queue.popleft()[1])
        return time


tasks = ["A","A","A","B","B","B"]
n = 2
# Output: 8
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 2
# Output: 16
sol = Solution()
result = sol.leastInterval(tasks, n)
print(result)
