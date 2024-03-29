# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        count = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return count
# class Solution:
        # My solution
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#         self.cnt = {}
#         self.res = 0
#         self.mid = 0
#         for i in range(1, 10):
#             self.cnt[i] = 0
#         self.traverse(root)
#         return self.res
    
#     def traverse(self, root):
#         val = root.val
#         self.cnt[val] += 1
#         # check and update how many c should be put in the mid
#         if self.cnt[val] % 2 == 0:
#             self.mid -= 1
#         else:
#             self.mid += 1
            
#         if root.left:
#             self.traverse(root.left)
#         if root.right:
#             self.traverse(root.right)
#         if not root.right and not root.left:
#             if self.mid <= 1:
#                 # print("yes")
#                 self.res += 1
#         self.cnt[val] -= 1
        
#         # check and update how many c should be put in the mid
#         if self.cnt[val] % 2 == 0:
#             self.mid -= 1
#         else:
#             self.mid += 1
    
#     def isPalindromic(self):
#         mid = 0
#         for k in self.cnt:
#             if self.cnt[k] % 2 != 0:
#                 if mid:
#                     return False
#                 else:
#                     mid += 1
#         return True