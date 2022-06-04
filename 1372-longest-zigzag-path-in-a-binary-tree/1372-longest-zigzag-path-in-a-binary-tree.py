# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # print(root)
        # print()
        self.ans = 0
        root.val = 0
        self.travelTree(root, -1)
        # print(root)
        return self.ans
        
    def travelTree(self, root, direction):
        self.ans = max(root.val, self.ans)
        if direction == -1:
            if root.left is not None:
                root.left.val = 1
                self.travelTree(root.left, 0)
            if root.right is not None:
                root.right.val = 1
                self.travelTree(root.right, 1)
        elif direction == 0:
            if root.left is not None:
                root.left.val = 1
                self.travelTree(root.left, 0)
            if root.right is not None:
                root.right.val = root.val + 1
                self.travelTree(root.right, 1)
        elif direction == 1:
            if root.left is not None:
                root.left.val = root.val + 1
                self.travelTree(root.left, 0)
            if root.right is not None:
                root.right.val = 1
                self.travelTree(root.right, 1)
                