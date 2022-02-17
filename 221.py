#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import List
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        if not matrix[0]:
            return 0
        n = len(matrix[0])
        maxLength = 0
        prev = [0] * (n+1)
        array = [0] * (n+1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    array[j] = min(array[j], array[j-1], prev[j-1]) + 1
                    maxLength = max(array[j], maxLength)
                else:
                    array[j] = 0
            prev = array.copy()
        return maxLength * maxLength

# @lc code=end

m = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
sol = Solution()
print(sol.maximalSquare(m))

