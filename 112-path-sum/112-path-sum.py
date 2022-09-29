# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.res = False
        self.traverse(root, 0, targetSum)
        return self.res
        
    
    def traverse(self, root, total, target):
        if self.res:
            return
        if root and not root.left and not root.right:
            if total + root.val == target:
                self.res = True
            return
        elif not root:
            return
        # print("traval to ", root.val, total)
        self.traverse(root.left, total + root.val, target)
        self.traverse(root.right, total + root.val, target)