import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}


def init_distance(graph, s):
    dist = {s: 0}
    for node in graph:
        if node != s:
            dist[node] = math.inf
    return dist


def dijkstra(graph, s):
    pri_queue = []
    heapq.heappush(pri_queue, (0, s))
    distance_map = init_distance(graph, s)
    seen = set()
    parent_map = {s: None}

    while len(pri_queue) > 0:
        dist, node = heapq.heappop(pri_queue)
        seen.add(node)
        adj_nodes = graph[node].keys()

        for adj_node in adj_nodes:
            acc_dist = dist + graph[node][adj_node]
            if adj_node not in seen and acc_dist < distance_map[adj_node]:
                heapq.heappush(pri_queue, (acc_dist, adj_node))
                distance_map[adj_node] = dist + graph[node][adj_node]
                parent_map[adj_node] = node

    return parent_map


print(dijkstra(graph, "A"))
