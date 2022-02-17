#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        answer = []
        line = []
        p = []
        q = []
        if root:
            p.append(root)
        while p:
            node = p.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            line.append(node.val)
            if not p:
                p = q
                q = []
                answer.append(line)
                line = []
        answer.reverse()
        return answer
# @lc code=end

