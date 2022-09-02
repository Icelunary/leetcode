# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.res = []
        self.levelNum = []
        self.reachedLevel = -1
        self.traverse(root, 0)
        self.calculateAve()
        return self.res
        
    def traverse(self, root, level):
        if self.reachedLevel < level:
            self.reachedLevel += 1
            self.res.append(0)
            self.levelNum.append(0)
        self.res[level] += root.val
        self.levelNum[level] += 1
        if root.left is not None:
            self.traverse(root.left, level + 1)
        if root.right is not None:
            self.traverse(root.right, level + 1)
            
    def calculateAve(self):
        for i in range(len(self.res)):
            self.res[i] = round(self.res[i] / self.levelNum[i], 5)