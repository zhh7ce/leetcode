#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.dic = dict()
        self.recurrsion(root)
        key = []
        value = 0
        for i,j in self.dic.items():
            if value == j:
                key.append(i)
            if value < j:
                key = [i]
                value = j
        return key

    def recurrsion(self, root):
        if root.val in self.dic:
            self.dic[root.val] += 1
        else:
            self.dic[root.val] = 1
        if root.left:
            self.recurrsion(root.left)
        if root.right:
            self.recurrsion(root.right)
# @lc code=end

