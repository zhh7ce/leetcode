#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.dic = dict()
        self.mid = True
        self.recursion(root, k)
        for i in self.dic.values():
            if i in self.dic:
                return True
        return False
    
    def recursion(self, root, k):
        if root:
            self.dic[root.val] = k - root.val
            if self.mid and root.val == k - root.val:
                self.dic.pop(root.val)
                self.mid = False
            self.recursion(root.left, k)
            self.recursion(root.right, k)
# @lc code=end

node = TreeNode(1)
s = Solution()
print(s.findTarget)