#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        tmp = self
        while tmp:
            print(tmp.val)
            tmp = tmp.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = ListNode()
        root.next = head
        tmp = root
        s = set()
        while tmp.next:
            if tmp.next.val in s:
                tmp.next = tmp.next.next
            else:
                s.add(tmp.next.val)
                tmp = tmp.next
        return root.next

# @lc code=end

