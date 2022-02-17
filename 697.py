#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()
        for index, val in enumerate(nums):
            if val in d:
                d[val][0] += 1
                d[val][2] = index
            else:
                d[val] = [1, index, index]
        count = 1
        ans = 1
        for c, first, last in d.values():
            if c == count:
                ans = min(ans, last - first + 1)
            elif c > count:
                ans = last - first + 1
                count = c
        return ans
# @lc code=end

