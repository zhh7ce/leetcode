
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left = root
        while left.left:
            left = left.left
        # right = root
        # while right.right:
        #     right = right.right
        right = self.recursion(root, True)
        right.right = left
        left.left = right
        return left

    def recursion(self, node, isLeft):
        """
        left: bool, Is the left child of its father
        for every left child, we need to return its rightest node
        for every right child, we need to return its leftest node
        """
        if node.left:
            left = self.recursion(node.left, True)
            left.right = node
            node.left = left
        if node.right:
            right = self.recursion(node.right, False)
            node.right = right
            right.left = node
        
        if isLeft:
            right = node
            while right.right:
                right = right.right
            return right
        else:
            left = node
            while left.left:
                left = left.left
            return left

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(12)
root.right.right = Node(17)

s = Solution()
n = s.treeToDoublyList(root)
for i in range(7):
    print(n.val)
    n = n.right