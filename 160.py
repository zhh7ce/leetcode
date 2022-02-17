#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i = headA
        j = headB
        while i and j:
            i = i.next
            j = j.next
        if i:
            j = headA
            while i:
                i = i.next
                j = j.next
            i = headB
        else:
            i = headB
            while j:
                i = i.next
                j = j.next
            j = headA
        while i and j:
            if i == j:
                return i
            i = i.next
            j = j.next
        return None
# @lc code=end

