#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: (x[0], x[1]))
        end = points[0][1]
        count = 1
        print(points)
        for i in points:
            if i[0] > end:
                count += 1
                end = i[1]
            else:
                end = min(end, i[1])
        return count
# @lc code=end
nums = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
s = Solution()
print(s.findMinArrowShots(nums))
