# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None
        self.traverse(cloned, target)
        return self.res
    
    def traverse(self, root, target):
        if root is None:
            return
        if root.val == target.val:
            self.res = root
        
        self.traverse(root.right, target)
        self.traverse(root.left, target)