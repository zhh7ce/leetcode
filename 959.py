#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
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

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        d = DSU(n*n*4)
        for i in range(n):
            for j in range(n):
                k = i*n*4 + j*4
                if grid[i][j] != '\\':
                    d.union(k, k+3)
                    d.union(k+1, k+2)
                if grid[i][j] != '/':
                    d.union(k, k+1)
                    d.union(k+2, k+3)
                if i != n-1:
                    d.union(k+2, k+n*4-4)
                if j != n-1:
                    d.union(k+1, k+7)
        return d.size
# @lc code=end

