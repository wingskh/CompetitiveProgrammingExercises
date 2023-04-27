# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append((root, 0))
        right_side_list = {}
    
        while len(queue) > 0:
            node, height = queue.popleft()
            if not node:
                continue
            if height not in right_side_list:
                right_side_list[height] = node.val

            if node.right:
                queue.append((node.right, height+1))
            elif node.left:
                queue.append((node.left, height+1))
                
        return [right_side_list[i] for i in range(len(right_side_list))]


def list_to_treenode(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = i % 2 == 0
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node
     

root = [1,2,3,None,5,None,4]
root = list_to_treenode(root)
sol = Solution()
result = sol.rightSideView(root)
print(result)
