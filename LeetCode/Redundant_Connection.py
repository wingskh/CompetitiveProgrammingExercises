# https://leetcode.com/problems/redundant-connection/

from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        edges = edges[::-1]
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        for edge in edges:
            stack = [(edge[1], edge[0])]
            seen = set([edge[0]])
            while stack:
                current, parent = stack.pop()
                for neighbor in adj_map[current]:
                    if neighbor == parent:
                        continue

                    if neighbor in seen:
                        if edge[0] == neighbor:
                            return edge
                        else:
                            stack = []
                            break
                    else:
                        seen.add(neighbor)
                        stack.append((neighbor, current))

        return []


edges = [[1, 2], [1, 3], [2, 3]]
# Output: [2, 3]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
# Output: [1, 4]
edges = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
# Output: [2, 5]
edges = [
    [9, 10],
    [5, 8],
    [2, 6],
    [1, 5],
    [3, 8],
    [4, 9],
    [8, 10],
    [4, 10],
    [6, 8],
    [7, 9],
]
# Output = [4, 10]
solution = Solution()
print(solution.findRedundantConnection(edges))
