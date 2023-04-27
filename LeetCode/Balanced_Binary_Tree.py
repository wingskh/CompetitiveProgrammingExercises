# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_if_balance(node, acc_height):
            lt_height = rt_height = acc_height
            balanced_lt, balanced_rt = True, True

            if node.left is not None:
                lt_height += 1
                balanced_lt, lt_height =  check_if_balance(node.left, lt_height)

            if node.right is not None:
                rt_height += 1
                balanced_rt, rt_height =  check_if_balance(node.right, rt_height)

            return (balanced_lt and balanced_rt and abs(lt_height - rt_height) < 2), max(lt_height, rt_height)

        return True if root is None else check_if_balance(root, 0)[0]

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
     

# root = [3,9,20,None,None,15,7]
root = [1,2,2,3,3,None,None,4,4]
# root = [1,None,2,None,3]
# root = [1,2,3,4,5,6,None,8]
root = list_to_treenode(root)
sol = Solution()
result = sol.isBalanced(root)
print(result)
