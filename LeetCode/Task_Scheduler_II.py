# https://leetcode.com/problems/task-scheduler-ii/
# https://leetcode.com/problems/task-scheduler-ii/discuss/2388526/python-easily-understood-faster-than-98-simple-o0
import math
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        count_dict = {}
        total_days = 0
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = -math.inf
            total_days = max(total_days + 1, count_dict[task] + space + 1)
            count_dict[task] = total_days
        return total_days
    
tasks = [5,8,8,5]
space = 2
sol = Solution()
print(sol.taskSchedulerII(tasks, space))