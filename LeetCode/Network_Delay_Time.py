# https://leetcode.com/problems/network-delay-time/

from typing import List
from collections import defaultdict
import math
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, target, weight in times:
            graph[source][target] = weight

        distance_map = {i: math.inf for i in range(1, n + 1)}
        distance_map[k] = 0
        pri_queue = []
        heapq.heappush(pri_queue, (0, k))
        seen = set()
        parent_map = {k: None}
        while len(pri_queue) > 0:
            dist, node = heapq.heappop(pri_queue)
            seen.add(node)
            adj_nodes = graph[node].keys()
            for adj_node in adj_nodes:
                acc_dist = dist + graph[node][adj_node]
                # print(node, adj_node, acc_dist, distance_map[adj_node], adj_node not in seen)
                if adj_node not in seen and acc_dist < distance_map[adj_node]:
                    heapq.heappush(pri_queue, (acc_dist, adj_node))
                    distance_map[adj_node] = acc_dist
                    parent_map[adj_node] = node

        max_dist = max(distance_map.values())
        return max_dist if max_dist != math.inf else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# Output: 2
times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
n = 3
k = 1
# Output: 3
times = [[1, 2, 1], [2, 3, 2], [1, 3, 1]]
n = 3
k = 2
# Output: -1
sol = Solution()
print(sol.networkDelayTime(times, n, k))

math.inf == math.inf
