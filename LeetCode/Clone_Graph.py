# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def dfs(node):
            nonlocal seen
            if node.val in seen:
                return seen[node.val]
            
            n = Node(node.val)
            seen[node.val] = n
            if node.neighbors is None:
                return n
                
            n.neighbors = []
            for child_node in node.neighbors:
                clone_child = dfs(child_node)
                n.neighbors.append(clone_child)
                
            return n
        
        if node is None:
            return None
        seen = dict()
        root = dfs(node)
        return root
