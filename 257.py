#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        arr = self.subQ(root)
        ans = []
        for i in arr:
            i.reverse()
            ans.append('->'.join(i))
        return ans
        
    def subQ(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return [[str(root.val)]]
        x = self.subQ(root.left)
        y = self.subQ(root.right)
        ans = []
        if x:
            for i in x:
                i.append(str(root.val))
                ans.append(i)
        if y:
            for i in y:
                i.append(str(root.val))
                ans.append(i)
        return ans
# @lc code=end

