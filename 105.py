#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        return self.recursion(inorder)

    def recursion(self, inorder):
        if not inorder:
            return None
        rootValue = 0
        for i in self.preorder:
            if  i in inorder:
                rootValue = i
                break
        self.preorder.remove(rootValue)
        rootIndex = inorder.index(rootValue)
        leftInOrder = inorder[:rootIndex]
        rightInOrder = inorder[rootIndex+1:]
        root = TreeNode(rootValue)
        root.left = self.recursion(leftInOrder)
        root.right = self.recursion(rightInOrder)
        return root
# @lc code=end
