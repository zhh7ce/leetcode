#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        d = DSU(n)
        for i in range(n):
            for j in range(i+1, n):
                if not d.isConnected(i, j) and self.check(strs[i], strs[j]):
                    d.union(i, j)
        return d.size
    
    def check(self, x, y):
        count = 0
        for (i, j) in zip(x, y):
            if i != j:
                count += 1
                if count > 2:
                    return False
        return True

# @lc code=end

