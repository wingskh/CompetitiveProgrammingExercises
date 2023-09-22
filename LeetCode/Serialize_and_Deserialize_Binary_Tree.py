# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
import sys
sys.path.append('../')
from Useful_Function.TreeNode import list_to_treenode
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # print('1 -----------------------')
            # print(node.val)
            # print(node.left)
            # print(node.right)
            # print('2 -----------------------')
            if node:
                queue.append(node.left)
                queue.append(node.right)
            result.append('None' if node is None else str(node.val))
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        elements = data.split(',')
        elements = [None if x == 'None' else int(x) for x in elements]
        root_node = None if elements[0] == None else TreeNode(elements[0])
        nodes = [root_node]
        for i, x in enumerate(elements[1:]):
            if x == None:
                continue
            parent_node = nodes[i // 2]
            is_left = i % 2 == 0
            node = TreeNode(x)
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node
            nodes.append(node)

        return root_node
        

# Your Codec object will be instantiated and called as such:
root = [1,2,3,None,None,4,5]
# root = [1,2,3,None,None,4,5, 1, 2]
root = list_to_treenode(root)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
# ans = ser.serialize(root)
print(ans)