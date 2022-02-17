#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
from typing import List
# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m+1):
            self.m.append([0] * (n+1))
        for i in range(m):
            for j in range(n):
                self.m[i][j] = self.m[i][j-1] + self.m[i-1][j] + matrix[i][j] - self.m[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.m[row2][col2] - self.m[row2][col1-1] - self.m[row1-1][col2] + self.m[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

matrix = [[-1]]
sol = NumMatrix(matrix)
print(sol.sumRegion(0,0,0,0))
