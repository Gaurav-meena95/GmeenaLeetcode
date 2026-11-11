# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def fn(root):
            if not root:
                return 0
            left = 1 + fn(root.left)
            right = 1 + fn(root.right)
            return max(left,right)
        return fn(root)