#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m = max(p.val, q.val)
        n = min(p.val, q.val)
        return self.subQ(root, m, n)
    
    def subQ(self, root, m, n):
        if m < root.val:
            return self.subQ(root.left, m, n)
        if n > root.val:
            return self.subQ(root.right, m, n)
        return root
# @lc code=end

