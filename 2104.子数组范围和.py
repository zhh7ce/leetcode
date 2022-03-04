#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            _min = nums[i]
            _max = nums[i]
            for j in range(i+1, n):
                if nums[j] < _min:
                    _min = nums[j]
                elif nums[j] > _max:
                    _max = nums[j]
                res += _max - _min
        return res
# @lc code=end

