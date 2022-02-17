#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        tmp = []
        ans = []
        line = []
        reverse = False
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            line.append(node.val)
            if not queue:
                queue = tmp
                tmp = []
                if reverse:
                    line.reverse()
                    reverse = False
                else:
                    reverse = True
                ans.append(line)
                line = []
        return ans
# @lc code=end

