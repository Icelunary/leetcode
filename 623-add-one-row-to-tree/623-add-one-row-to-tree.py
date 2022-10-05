# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.bfs(root, 1, val, depth)
    
    def bfs(self, root, d, val, depth):
        if not root:
            return None
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
        if d == depth - 1:
            left = root.left
            right = root.right
            root.left = TreeNode(val, left, None)
            root.right = TreeNode(val, None, right)
        else:
            self.bfs(root.left, d+1, val, depth)
            self.bfs(root.right, d+1, val, depth)
        return root