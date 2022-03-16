#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#

# @lc code=start
from readline import parse_and_bind


class Node:

    def __init__(self, left = None, right = None, s = '', val = 1) -> None:
        self.left = left
        self.right = right
        self.val = val
        self.s = s

class AllOne:

    def __init__(self):
        self.dict = dict()
        self.ll = Node(val=0)
        self.rr = Node(val=float('inf'))
        self.ll.right = self.rr
        self.rr.left = self.ll


    def inc(self, key: str) -> None:
        if key in self.dict:
            tmp = self.dict[key]
            tmp.val += 1
            dst = tmp.right
            while tmp.val > dst.val:
                dst = dst.right
            if dst != tmp.right:
                tmp.left.right = tmp.right
                tmp.right.left = tmp.left
                tmp.left = dst.left
                tmp.right = dst
                tmp.left.right = tmp
                tmp.right.left = tmp
        else:
            tmp = Node(self.ll, self.ll.right, key)
            self.dict[key] = tmp
            self.ll.right.left = tmp
            self.ll.right = tmp


    def dec(self, key: str) -> None:
        tmp = self.dict[key]
        if tmp.val == 1:
            tmp.left.right = tmp.right
            tmp.right.left = tmp.left
            del tmp
        else:
            tmp.val -= 1
            dst = tmp.left
            while tmp.val < dst.val:
                dst = dst.left
            if dst != tmp.left:
                tmp.left.right = tmp.right
                tmp.right.left = tmp.left
                tmp.left = dst
                tmp.right = dst.right
                tmp.left.right = tmp
                tmp.right.left = tmp


    def getMaxKey(self) -> str:
        return self.rr.left.s


    def getMinKey(self) -> str:
        return self.ll.right.s



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

