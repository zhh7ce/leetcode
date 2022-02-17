#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        self.recursion(root, 0)
        return self.sum

    def recursion(self, root, s):
        if not root:
            return
        s *= 2
        s += root.val
        if not root.left and not root.right:
            self.sum += s
            return
        self.recursion(root.left, s)
        self.recursion(root.right, s)
        return
# @lc code=end

