#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.arr = []
        self.recursion(root)
        return self.arr

    def recursion(self, root):
        if not root:
            return
        for i in root.children:
            self.recursion(i)
        self.arr.append(root.val)
# @lc code=end

