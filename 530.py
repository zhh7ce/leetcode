#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.arr = []
        self.inOrder(root)
        diff = float('inf')
        for i in range(len(self.arr)-1):
            diff = min(diff, self.arr[i+1] - self.arr[i])
        return diff

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)
# @lc code=end

