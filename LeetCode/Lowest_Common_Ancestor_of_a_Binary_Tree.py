# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root):
        if root is None:
            return 0

        score = 1 if root.val in self.target else 0
        acc_sum = self.dfs(root.left) + self.dfs(root.right) + score
        if acc_sum == 2:
            self.ans = root
            raise
        return acc_sum
            

    def lowestCommonAncestor(self, root, p, q):
        self.target = set([p.val, q.val])
        self.ans = None
        try:
            self.dfs(root)
        except:
            return self.ans


def from_list(elements):
    root_node = TreeNode(x=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(x=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


node_list = [3,5,1,6,2,0,8,None,None,7,4]
p = TreeNode(5)
q = TreeNode(1)
root = from_list(node_list)

sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))
