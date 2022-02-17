#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.subQ(root, False)

    def subQ(self, root, left):
        if not root:
            return 0
        if not root.left and not root.right:
            if left:
                return root.val
            else:
                return 0
        return self.subQ(root.left, True) + self.subQ(root.right, False)
# @lc code=end

