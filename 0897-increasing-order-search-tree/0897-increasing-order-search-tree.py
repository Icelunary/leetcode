# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
        
    def traverse(self, root, direction):
        if not root:
            return None
        left = self.traverse(root.left, 0)
        if left:
            left.next = root
        else:
            left = root
        right = self.traverse(root.right, 1)
        if right:
            root.next = right
        else:
            right = root
        return left if direction else right