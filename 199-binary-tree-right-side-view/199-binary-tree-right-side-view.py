# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.cnt = 0
        self.traverse(root,  0)
        return self.res
    
    def traverse(self, root, level):
        if root:
            if level == self.cnt:
                self.res.append(root.val)
                self.cnt += 1
            if root.right:
                self.traverse(root.right, level + 1)
            if root.left:
                self.traverse(root.left, level + 1)