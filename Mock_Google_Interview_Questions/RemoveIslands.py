# https://www.youtube.com/watch?v=4tYoVx0QoN0&t=426s&ab_channel=Cl%C3%A9mentMihailescu
from collections import deque 

def bfs(matrix, s, seen, max_size):
    global total_rows, total_colums
    queue = deque()
    queue.append(s)
    seen.add(s)
    total_rows, total_colums = max_size
    while len(queue) > 0:
        r, c = queue.popleft()
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            adj_r, adj_c = r + i[0], c + i[1]
            if adj_r < 0 or adj_c < 0 or adj_r > total_rows - 1 or adj_c > total_colums - 1:
                continue

            if matrix[adj_r][adj_c] == 1 and (adj_r, adj_c) not in seen:
                queue.append((adj_r, adj_c))
                seen.add((adj_r, adj_c))


def removeIslands(matrix):
    global total_rows, total_colums

    total_rows = len(matrix)
    total_colums = len(matrix[0])
    seen = set()
    for r in range(total_rows):
        for c in range(total_colums):
            if r == [0, total_rows-1] or c in [0, total_colums-1]:
                if matrix[r][c] == 1:
                    bfs(matrix, (r, c), seen, (total_rows, total_colums))
    
    for r in range(1, total_rows-1):
        for c in range(1, total_colums-1):
            if (r, c) not in seen:
                matrix[r][c] = 0
    for i in matrix:
        print(i)


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]
removeIslands(matrix)