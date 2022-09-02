# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.traverse(root, 0)
        return root
        
    def traverse(self, root, parentSum):
        rightSum = 0
        leftSum = 0
        val = root.val
        if root.right:
            rightSum = self.traverse(root.right, parentSum)
        root.val = root.val + rightSum + parentSum
        if root.left:
            parentSum = root.val
            leftSum = self.traverse(root.left, parentSum)
        return rightSum + leftSum + val
        