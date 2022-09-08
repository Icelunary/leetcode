# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root.left:
            self.traverse(root.left)
        self.res.append(root.val)
        if root.right:
            self.traverse(root.right)           