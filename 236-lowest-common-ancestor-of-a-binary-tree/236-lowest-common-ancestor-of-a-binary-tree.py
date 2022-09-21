# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def bfs(root, a, b):
            if not root:
                return 0
            l = bfs(root.left, a, b)
            r = bfs(root.right, a, b)
            here = 0
            if root.val == a:
                here += 1
            elif root.val == b:
                here += 2
            if here + l + r == 3 and self.ans is None:
                self.ans = root
            return l + here + r
        
        bfs(root, p.val, q.val)
        return self.ans