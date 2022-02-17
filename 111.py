#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        root.val = 1
        while q:
            node = q.pop(0)
            if node.left or node.right:
                if node.left:
                    node.left.val = node.val + 1
                    q.append(node.left)
                if node.right:
                    node.right.val = node.val + 1
                    q.append(node.right)
            else:
                return node.val
# @lc code=end

