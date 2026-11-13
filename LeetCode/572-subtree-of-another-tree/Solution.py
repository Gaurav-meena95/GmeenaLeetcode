# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def fn(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and fn(p.left,q.left) and fn(p.right,q.right)
        if not root:
            return False
        return fn(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)