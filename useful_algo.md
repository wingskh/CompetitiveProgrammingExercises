**Floyd's Cycle-Finding Algorithm**
Usage: `Find if cycle existed in a list node`
Remark: `according to Floyd's cycle detection algorithm, when both pointers move at the same speed, they will eventually meet at the starting point of the cycle.`

Example:

```
1. LeetCode/Linked_List_Cycle.py
1. LeetCode/Find_the_Duplicate_Number.py
```

**Dijkstras Shortest Path/BFS**
Usage: `Find the shortest paths in a graph`

**Hierholzer's Algorithm**
Usage: `Find Eulerian paths or circuits in a directed or undirected graph`
Euler path: `a path that uses every edge of a graph exactly once`
Euler circuit: `a circuit that uses every edge of a graph exactly once`

**Kruskal's Algorithm**
Usage: `find the Minimum Spanning Tree (MST), or Minimum Spanning Forest`

```
1. Sort all edges by weight
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
3. If cycle is not formed, include this edge. Else, discard it.
4. Repeat step 2 until there are (V-1) edges in the spanning tree.
```
