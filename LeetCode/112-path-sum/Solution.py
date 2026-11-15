# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def fn(root,currsum):
            if not root:
                return False
            currsum += root.val
            if not root.left and not root.right:
                return currsum == targetSum
            return fn(root.left,currsum) or fn(root.right,currsum)
        return fn(root,0)