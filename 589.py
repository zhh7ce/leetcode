#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.ans = []
        self.recursion(root)
        return self.ans
    
    def recursion(self, root):
        self.ans.append(root.val)
        for i in root.children:
            self.recursion(i)
# @lc code=end

