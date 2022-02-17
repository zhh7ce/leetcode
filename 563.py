#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.sum = 0
        self.recursion(root)
        return self.sum

    def recursion(self, root):
        if not root:
            return 0
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        self.sum += abs(left - right)
        return left + right + root.val
# @lc code=end

