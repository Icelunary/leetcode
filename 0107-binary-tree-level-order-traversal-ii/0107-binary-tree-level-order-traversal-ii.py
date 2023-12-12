# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.dfs(ans, root, 0)
        return ans[::-1]
    
    def dfs(self, ans: List[List[int]], root: Optional[TreeNode], level: int):
        if len(ans) <= level:
            ans.append([])
        
        ans[level].append(root.val)
        if root.left:
            self.dfs(ans, root.left, level + 1)
        if root.right:
            self.dfs(ans, root.right, level + 1)
        