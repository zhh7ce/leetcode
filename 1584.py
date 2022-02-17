#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start
import heapq

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = DSU(n)
        ans = 0
        q = []
        for i in range(n):
            for j in range(i+1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(q, (dis, (i, j)))
        while d.size > 1:
            dis, (i, j) = heapq.heappop(q)
            if not d.isConnected(i, j):
                ans += dis
                d.union(i, j)
        return ans

# @lc code=end

