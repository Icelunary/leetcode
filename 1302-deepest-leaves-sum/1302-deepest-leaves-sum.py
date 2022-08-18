# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level_list = [root]
        total = 0
        # for i in range(len(level_list)):
        #     level_list.append(root)
        #     print(i)
        # print(len(level_list))
        
        while level_list:
            total = 0
            print("length: ", len(level_list))
            for i in range(len(level_list)):
                total += level_list[0].val
                if (level_list[0].left is not None): level_list.append(level_list[0].left)
                if (level_list[0].right is not None): level_list.append(level_list[0].right)
                del level_list[0]
            print(total)
        print(total)
        return total