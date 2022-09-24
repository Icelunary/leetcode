# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.cur = []
        self.sum = 0
        self.paths = []
        self.traverse(root, targetSum)
        return self.paths
    
    def traverse(self, root, target):
        if not root:
            return
        self.cur.append(root.val)
        self.sum += root.val
        if self.isLeaf(root) and self.sum == target:
            self.paths.append(self.cur.copy())
        self.traverse(root.left, target)
        self.traverse(root.right, target)
        self.sum -= self.cur.pop()
    
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        else:
            return False