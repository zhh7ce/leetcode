#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.setDepth(root)
        return self.findMax(root)

    def setDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            root.val = 1
            return 1
        root.val = max(self.setDepth(root.left), self.setDepth(root.right)) + 1
        return root.val

    def findMax(self, root):
        if not root:
            return 0
        x = self.findMax(root.left)
        y = self.findMax(root.right)
        z = 0
        if root.left:
            z += root.left.val
        if root.right:
            z += root.right.val
        return max(x, y, z)
        
# @lc code=end

