#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            root.val = 1
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            m = 0
            n = 0
            if root.left:
                m = root.left.val
            if root.right:
                n = root.right.val
            root.val = max(m, n) + 1
            return abs(m - n) <= 1
        else:
            return False
        
# @lc code=end

