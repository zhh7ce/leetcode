#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        arr = []
        while fast:
            arr.append(slow.val)
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                arr.pop()
        i = 1
        while slow:
            if slow.val != arr[-i]:
                return False
            slow = slow.next
            i += 1
        return True
        
# @lc code=end

