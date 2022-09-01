# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, -math.inf)
        return self.cnt
        
    def traverse(self, node, num):
        big1 = max(node.val, num)
        if node.val >= num:
            self.cnt += 1
        if node.left != None:
            self.traverse(node.left, big1)
        if node.right != None:
            self.traverse(node.right, big1)
        