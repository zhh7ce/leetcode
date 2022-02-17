#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        x = self.getLeaf(root1)
        y = self.getLeaf(root2)
        if x != y:
            return False
        return True
    
    def getLeaf(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return [node.val]
        x = self.getLeaf(node.left)
        y = self.getLeaf(node.right)
        z = []
        if x:
            z.extend(x)
        if y:
            z.extend(y)
        return z
# @lc code=end

