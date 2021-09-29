import heapq
import math

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D':6},
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
    distance = init_distance(graph, s)
    seem = set()
    parent = {s: None}

    while len(pri_queue) > 0:
        dist, node = heapq.heappop(pri_queue)
        seem.add(node)
        nodes = graph[node].keys()

        for n in nodes:
            acc_dist = dist + graph[node][n]
            if n not in seem and acc_dist < distance[n]:
                heapq.heappush(pri_queue, (acc_dist, n))
                distance[n] = dist + graph[node][n]
                parent[n] = node

    return parent

print(dijkstra(graph, 'A'))
