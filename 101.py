#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isOpp(root.left, root.right)
    
    def isOpp(self, x, y):
        if not x or not y:
            if not x and not y:
                return True
            else:
                return False
        return x.val == y.val and self.isOpp(x.left, y.right) and self.isOpp(x.right, y.left)
# @lc code=end

