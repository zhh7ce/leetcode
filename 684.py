#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

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
    
    def isConnected(self, x, y):
        a = self.find(x)
        b = self.find(y)
        return a == b

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for e in edges:
            n = max(e[1], n)
        d = DSU(n+1)
        ans = [0, 0]
        for e in edges:
            if d.isConnected(e[0], e[1]):
                ans = e
            else:
                d.union(e[0], e[1])
        return ans
        
# @lc code=end

