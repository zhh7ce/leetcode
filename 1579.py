#
# @lc app=leetcode.cn id=1579 lang=python3
#
# [1579] 保证图可完全遍历
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
    
    def check(self, x, y):
        a = self.find(x)
        b = self.find(y)
        return a == b

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = DSU(n+1)
        b = DSU(n+1)
        ans = 0
        for [t, u, v] in edges:
            if t == 3:
                if a.check(u, v) and b.check(u, v):
                    ans += 1
                else:
                    a.union(u, v)
                    b.union(u, v)
        for [t, u, v] in edges:
            if t == 1:
                if a.check(u, v):
                    ans += 1
                else:
                    a.union(u, v)
            elif t == 2:
                if b.check(u, v):
                    ans += 1
                else:
                    b.union(u, v)
        if a.size == 2 and b.size == 2:
            return ans
        else:
            return -1

# @lc code=end

