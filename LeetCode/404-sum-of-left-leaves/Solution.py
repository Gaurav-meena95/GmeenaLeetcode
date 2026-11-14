# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        ans = [0]
        def fn(root):
            if not root:
                return 
            if root.left and not root.left.left and not root.left.right:
                ans[0] += root.left.val
            fn(root.left)
            fn(root.right)
        fn(root)
        return ans[0]