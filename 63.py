#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        array = [1] * (n + 1)
        array[-1] = 0
        for i in range(n):
            if obstacleGrid[0][i]:
                for j in range(i, n):
                    array[j] = 0
        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    array[j] = 0
                else:
                    array[j] += array[j-1]
        return array[-2]
# @lc code=end
m = [[0,0,0],[1,1,0],[0,0,0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(m))
