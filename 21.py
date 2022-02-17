#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        tmp = root
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        while l1:
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next
        while l2:
            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next
        return root.next
        


        
# @lc code=end

if __name__ == "__main__":
    n0 = ListNode(1)
    n0.next = ListNode(2)
    n0.next.next = ListNode(4)
    n1 = ListNode(1)
    n1.next = ListNode(3)
    n1.next.next = ListNode(4)

    s = Solution()
    s.mergeTwoLists(n0, n1).print()
