#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        res = [0] * n
        for i in range(n):
            row = 0
            column = i
            while row < m:
                if column == 0:
                    if grid[row][column] == -1:
                        column = -1
                        break
                if column == n-1:
                    if grid[row][column] == 1:
                        column = -1
                        break
                if grid[row][column] == 1 and grid[row][column+1] == -1:
                    column = -1
                    break
                if grid[row][column] == -1 and grid[row][column-1] == 1:
                    column = -1
                    break
                column += grid[row][column]
                row += 1
            res[i] =  column
        return res
# @lc code=end

