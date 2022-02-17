#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xDepth, xFather = self.findQ(root, x)
        yDepth, yFather = self.findQ(root, y)
        if xDepth == yDepth and xFather != yFather:
            return True
        return False

    def findQ(self, root, x):
        if not root:
            return 0, 0
        if root.val == x:
            return 1, 0
        xDepth, xFather = self.findQ(root.left, x)
        if xDepth == 1:
            return xDepth+1, root.val
        if xDepth:
            return xDepth+1, xFather
        xDepth, xFather = self.findQ(root.right, x)
        if xDepth == 1:
            return xDepth+1, root.val
        if xDepth:
            return xDepth+1, xFather
        return 0, 0
# @lc code=end

