# https://leetcode.com/problems/validate-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_validate(root, lower, upper):
            if not root:
                return True
            if lower >= root.val or upper <= root.val:
                return False
            else:
                return check_validate(root.left, lower, root.val) and check_validate(
                    root.right, root.val, upper
                )

        return check_validate(root, -math.inf, math.inf)

    last = -math.inf
    ended = False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_validate(cur):
            if self.ended:
                return
            if cur.left:
                check_validate(cur.left)

            if not (cur.val > self.last):
                self.ended = True
                return

            self.last = cur.val
            if cur.right:
                check_validate(cur.right)

        check_validate(root)
        return not self.ended
