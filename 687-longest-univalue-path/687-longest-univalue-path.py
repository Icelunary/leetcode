# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.traverse(root, None)
        return self.cnt
    
    def traverse(self, root, parentVal):
        if not root:
            return 0
        right =  self.traverse(root.right, root.val)
        left = self.traverse(root.left, root.val)
        oneLine = max(left, right)
        double = left + right
        self.cnt = max(self.cnt, oneLine, double)
        if root.val == parentVal:
            return oneLine + 1
        else:
            return 0