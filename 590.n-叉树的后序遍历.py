#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
        if root == None:
            return []
        stack = []
        temp = [root]
        res = []
        while temp:
            node = temp.pop()
            stack.append(node)
            if node.children == None:
                continue
            for i in node.children:
                temp.append(i)
        while stack:
            node = stack.pop()
            res.append(node.val)
        return res


        
# @lc code=end

