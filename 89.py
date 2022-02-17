#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
from typing import List
# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        self.weight = [1] * n
        for i in range(1, n):
            self.weight[i] = self.weight[i-1] * 2
        return self.recursion(n)
    
    def recursion(self, n):
        if n == 1:
            return [0, 1]
        array = self.recursion(n-1)
        res = []
        zero = True
        for i in array:
            if zero:
                res.append(i)
                res.append(i+self.weight[n-1])
                zero = False
            else:
                res.append(i+self.weight[n-1])
                res.append(i)
                zero = True
        return res
# @lc code=end

s = Solution()
print(s.grayCode(1))