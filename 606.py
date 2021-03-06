#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        x = self.tree2str(t.left)
        y = self.tree2str(t.right)
        ans = str(t.val)
        if x != '' or y != '':
            ans += '('
            ans += x
            ans += ')'
        if y != '':
            ans += '('
            ans += y
            ans += ')'
        return ans
# @lc code=end

