# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        self.traverse(root)
        return self.res
        
    def traverse(self, root):
        self.res += str(root.val)
        if root.left:
            self.res += "("
            self.traverse(root.left)
            self.res += ")"
        elif root.right:
            self.res += "()"
        if root.right:
            self.res += "("
            self.traverse(root.right)
            self.res += ")"
