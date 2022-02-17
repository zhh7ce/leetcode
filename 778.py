#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        s = set()
        s.add(grid[0][0])
        heapq.heappush(q, (grid[0][0], (0, 0)))
        while True:
            cost, (x, y) = heapq.heappop(q)
            if x == n-1 and y == n-1:
                return cost
            if x != 0:
                if grid[x-1][y] not in s:
                    heapq.heappush(q, (max(cost, grid[x-1][y]), (x-1, y)))
                    s.add(grid[x-1][y])
            if x != n-1:
                if grid[x+1][y] not in s:
                    heapq.heappush(q, (max(cost, grid[x+1][y]), (x+1, y)))
                    s.add(grid[x+1][y])
            if y != 0:
                if grid[x][y-1] not in s:
                    heapq.heappush(q, (max(cost, grid[x][y-1]), (x, y-1)))
                    s.add(grid[x][y-1])
            if y != n-1:
                if grid[x][y+1] not in s:
                    heapq.heappush(q, (max(cost, grid[x][y+1]), (x, y+1)))
                    s.add(grid[x][y+1])

# @lc code=end

