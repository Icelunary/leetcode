# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.path = ""
        self.find = False
        self.traverse(root, startValue, destValue, "")
        return self.path
        
    def traverse(self, root: Optional[TreeNode], s: int, dest: int, direction: str) -> str:
        if not root:
            return 0, ""
        if self.find:
            return 0, ""
        this_path = ""
        find = 0
        if root.val == s:
            find = 1
        elif root.val == dest:
            find = 2
            
        #find l and r path
        find1, lpath = self.traverse(root.left, s, dest, "L")
        find2, rpath = self.traverse(root.right, s, dest, "R")
        
        # == 3 means found all
        if find1 + find2 + find == 3 and not self.find:
            self.find = True
            # print("root.val", root.val, "pathL", lpath, "pathR", rpath, s, root.val == s)
            # if this node is start, we dont need to reverse the path
            if root.val == s:
                self.path = lpath + rpath
            # if this node is dest, we need to reverse the path to "U"
            elif root.val == dest:
                path = lpath + rpath
                for c in path:
                    self.path += "U"
            # if this ancestor node is other node, reverse the path where we find s
            else:
                if find1 == 1:
                    for c in lpath:
                        self.path += "U"
                    self.path += rpath
                else:
                    for c in rpath:
                        self.path += "U"
                    self.path += lpath
        
        if find1 + find2 + find:
            this_path = direction
        # print(root.val, lpath, "|", this_path, "|", rpath)
        return find1 + find2 + find, this_path + lpath + rpath
