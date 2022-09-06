# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.traverse(root)
        if not res:
            return None
        return root
        
    def traverse(self, root):
        if root is None:
            return 0
        right = self.traverse(root.right)
        left = self.traverse(root.left)
        if not right:
            root.right = None
        if not left:
            root.left = None
        if root.val:
            return 1
        else:
            if left == right == root.val == 0:
                root = None
            return max(left, right)