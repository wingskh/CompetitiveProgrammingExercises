# https://leetcode.com/problems/min-cost-to-connect-all-points/
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def findRoot(i):
            if i != parent_list[i]:
                parent_list[i] = findRoot(parent_list[i])
            return parent_list[i]

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def union(i, j):
            i_root = findRoot(i)
            j_root = findRoot(j)
            if i_root != j_root:
                if rank_list[i_root] < rank_list[j_root]:
                    parent_list[i_root] = j_root
                elif rank_list[i_root] >= rank_list[j_root]:
                    if rank_list[i_root] == rank_list[j_root]:
                        rank_list[i_root] += 1
                    parent_list[j_root] = i_root
                return True
            return False

        point_len = len(points)
        edges = [
            (manhattan_distance(points[i], points[j]), i, j)
            for i in range(point_len)
            for j in range(i + 1, point_len)
        ]
        edges.sort(reverse=True)
        rank_list = [0] * point_len
        parent_list = [i for i in range(point_len)]
        result = 0
        while len(edges) > 0:
            edge, i, j = edges.pop()
            is_union = union(i, j)
            if is_union:
                result += edge

        return result


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# Output: 20
points = [[3, 12], [-2, 5], [-4, 1]]
# # Output: 18
points = [[-1000000, -1000000], [1000000, 1000000]]
# Output: 4000000
sol = Solution()
print(sol.minCostConnectPoints(points))
