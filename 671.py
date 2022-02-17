#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        x = self.findDiff(root.left, root.val)
        y = self.findDiff(root.right, root.val)
        z = min(x, y)
        if z < float('inf'):
            return z
        else:
            return -1

    def findDiff(self, root, x):
        if not root:
            return float('inf')
        if root.val != x:
            return root.val
        x = self.findDiff(root.left, root.val)
        y = self.findDiff(root.right, root.val)
        return min(x,y)
# @lc code=end

