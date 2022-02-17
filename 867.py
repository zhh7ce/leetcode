#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                transposed[i][j] = matrix[j][i]
        return transposed
# @lc code=end

