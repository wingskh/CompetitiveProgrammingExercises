# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
from platform import node
from re import L


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def sortedArrayToBST(self, nums):
        total_nums = len(nums)
        if total_nums == 1:
            return TreeNode(nums[0])
        elif total_nums == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))
        elif total_nums == 3:
            return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))

        mid_node = total_nums // 2
        left = nums[:mid_node]
        right = nums[mid_node + 1 :]
        node = TreeNode(nums[mid_node], self.sortedArrayToBST(left), self.sortedArrayToBST(right))

        return node


    def sortedArrayToBST(self, nums):
        total_nums = len(nums)
        if total_nums == 0:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )



nums = [0, 1, 2, 3, 4, 5, 6, 7]
sol = Solution()
result = sol.self.sortedArrayToBST(nums)
print(result)
