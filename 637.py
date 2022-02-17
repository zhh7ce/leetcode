#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        q = []
        temp = []
        s = 0
        c = 0
        if root:
            q.append(root)
        while q:
            node = q.pop(0)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            s += node.val
            c += 1
            if not q:
                ans.append(s/c)
                q = temp
                temp = []
                s = 0
                c = 0
        return ans
# @lc code=end

