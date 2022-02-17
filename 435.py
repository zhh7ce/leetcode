#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:(x[1], x[0]))
        count = 0
        end = float('-inf')
        for i in intervals:
            if end <= i[0]:
                count += 1
                end = i[1]
        return len(intervals) - count
# @lc code=end
n = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
s = Solution()
print(s.eraseOverlapIntervals(n))
