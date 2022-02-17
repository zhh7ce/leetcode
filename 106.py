#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.len = len(postorder)
        return self.recursion(inorder)

    def recursion(self, inorder):
        if not inorder:
            return None
        rootValue = 0
        rootIndex = 0
        for i in range(-1, -self.len-1, -1):
            if self.postorder[i] in inorder:
                rootIndex = i
                rootValue = self.postorder[i]
                break
        else:
            return None
        self.postorder.pop(rootIndex)
        self.len -= 1
        rootIndex = inorder.index(rootValue)
        leftInorder = inorder[:rootIndex]
        rightInorder = inorder[rootIndex+1:]
        root = TreeNode(rootValue)
        root.left = self.recursion(leftInorder)
        root.right = self.recursion(rightInorder)
        return root
# @lc code=end

