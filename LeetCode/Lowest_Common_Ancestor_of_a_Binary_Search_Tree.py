# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/2414941/Python-oror-Detailed-Explanation-oror-Easily-Understood-oror-O(h)-oror-O(n)

# Definition for a binary tree node.
from re import T


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    inorder = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_lca(root, p, q):
            if root == p or root == q or root is None:
                return root
        
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)

            if left is not None and right is not None: 
                return root
            elif left is not None: 
                return left
            else:
                return right

        if p.val == q.val:
            return root

        return find_lca(root, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            min_val = p.val
            max_val = q.val
        else:
            min_val = q.val
            max_val = p.val

        while True:
            if min_val <= root.val <= max_val:
                return root
            elif max_val < root.val:
                root = root.left
            else:
                root = root.right


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

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
root = from_list(root)
p = TreeNode(p)
q = TreeNode(q)
sol = Solution()
result = sol.lowestCommonAncestor(root, p, q)
print(result)