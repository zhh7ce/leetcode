#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        _min = nums[0]
        n = len(nums)
        dp = -1
        for i in range(1, n):
            if nums[i] > _min:
                dp = max(dp, nums[i] - _min)
            else:
                _min = nums[i]
        return dp
# @lc code=end

