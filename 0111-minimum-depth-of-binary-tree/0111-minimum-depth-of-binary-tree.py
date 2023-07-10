# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode], depth:int = 0) -> int:
        # print(root.val, root.left.val if root.left else "None", root.right.val if root.right else "None", depth)
        if not root:
            return 0
        if not root.left and not root.right:
            return depth + 1
        left = right = float("inf")
        if root.left:
            left = self.minDepth(root.left, depth + 1)
        if root.right:
            right = self.minDepth(root.right, depth + 1)
        return min(left, right)