#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, tail = self.subQ(root)
        return head
        
    def subQ(self, root):
        if not root:
            return None, None
        if not root.left or not root.right:
            if root.left:
                lhead, ltail = self.subQ(root.left)
                ltail.right = root
                root.left = None
                return lhead, root
            if root.right:
                rhead, rtail = self.subQ(root.right)
                root.right = rhead
                return root, rtail
            return root, root
        lhead, ltail = self.subQ(root.left)
        rhead, rtail = self.subQ(root.right)
        ltail.right = root
        root.right = rhead
        root.left = None
        return lhead, rtail
# @lc code=end

