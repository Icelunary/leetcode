# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dis = {}
    parentToChild = {}
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.dis = {}
        self.parentToChild = {}
        self.topSort(descriptions)
        root_val = self.getRoot()
        root = TreeNode(root_val, None, None)
        self.construct(root)
        return root
        
    def topSort(self, descriptions):
        for relation in descriptions:
            parent = relation[0]
            child = relation[1]
            position = relation[2]
            info = (child, position)
            if parent in self.parentToChild:
                self.parentToChild[parent].append(info)
            else:
                self.parentToChild[parent] = [info]
            self.dis[child] = 1
            if parent not in self.dis:
                self.dis[parent] = 0
        
    def construct(self, parent):
        for child in self.parentToChild[parent.val]:
            val = child[0]
            position = child[1]
            node = TreeNode(val, None, None)
            if position:
                parent.left = node
            else:
                parent.right = node
            if val in self.parentToChild:
                self.construct(node)
        
    def getRoot(self):
        for i in self.dis:
            if self.dis[i] == 0:
                return i