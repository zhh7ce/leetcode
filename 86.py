#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        root = ListNode(x-1)
        root.next = head
        insert = root
        while insert.next and  insert.next.val < x:
            insert = insert.next
        pos = insert.next
        while pos
# @lc code=end

