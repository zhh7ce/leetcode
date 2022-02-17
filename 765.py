#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#
from typing import List
# @lc code=start
class DSU:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.size = n

    def find(self, k):
        if self.arr[k] == k:
            return k
        else:
            self.arr[k] = self.find(self.arr[k])
            return self.arr[k]
    
    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            self.arr[a] = b
            self.size -= 1
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        d = DSU(n)
        for i in range(0, n, 2):
            x = row[i]
            y = row[i+1]
            d.union(x, y)
            if x & 1:
                d.union(x, x-1)
            else:
                d.union(x, x+1)
            if y & 1:
                d.union(y, y-1)
            else:
                d.union(y, y+1)
        return (n >> 1) - d.size
# @lc code=end
s = Solution()
row = [3, 2, 0, 1]
print(s.minSwapsCouples(row))
