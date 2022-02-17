#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
#

# @lc code=start
class DSU(object):
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.number = n
    
    def find(self, k):
        if self.arr[k] == k:
            return k
        self.arr[k] = self.find(self.arr[k])
        return self.arr[k]

    def combine(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.arr[x] = y
            self.number -= 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        dsu = DSU()
        for [a, b] in connections:
            dsu.combine(a, b)
        return dus.number - 1
        
# @lc code=end

