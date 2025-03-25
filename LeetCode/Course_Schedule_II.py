# https://leetcode.com/problems/course-schedule-ii/

from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_as_prereq_map = defaultdict(list)
        in_degree = [0] * numCourses
        courses_with_no_prereqs = set(range(numCourses))

        for course, prereq in prerequisites:
            if course == prereq:
                return []
            courses_as_prereq_map[prereq].append(course)
            in_degree[course] += 1
            courses_with_no_prereqs.discard(course)

        queue = deque(courses_with_no_prereqs)

        if not queue:
            return []

        result = []
        while queue:
            current = queue.popleft()
            result.append(current)

            for available_dependent_course in courses_as_prereq_map[current]:
                in_degree[available_dependent_course] -= 1
                if in_degree[available_dependent_course] == 0:
                    queue.append(available_dependent_course)

        if len(result) != numCourses:
            return []

        return result


numCourses = 2
prerequisites = [[1, 0]]
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output: [0,2,1,3]
# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]
# Output: []
numCourses = 7
prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
# Output: [6,5,4,2,3,0,1]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))
