#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
class DSU(object):
    def __init__(self, n):
        self.arr = [i for i in range(n)]
    
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
    
    def isConnected(self, x, y):
        a = self.find(x)
        b = self.find(y)
        return a == b

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dic = dict()
        row = len(heights)
        col = len(heights[0])
        for i in range(row):
            for j in range(col-1):
                h = abs(heights[i][j] - heights[i][j+1])
                if h in dic:
                    dic[h].append((i*col+j, i*col+j+1))
                else:
                    dic[h] = [(i*col+j, i*col+j+1)]
        for i in range(row-1):
            for j in range(col):
                h = abs(heights[i][j] - heights[i+1][j])
                if h in dic:
                    dic[h].append((i*col+j, (i+1)*col+j))
                else:
                    dic[h] = [(i*col+j, (i+1)*col+j)]
        keys = list(dic.keys())
        keys.sort()
        n = row * col
        dsu = DSU(n)
        for k in keys:
            for (x, y) in dic[k]:
                dsu.union(x, y)
            if dsu.isConnected(0, n-1):
                return k
        return 0

# @lc code=end


