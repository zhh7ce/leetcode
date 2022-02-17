#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        array = [0] * (length + 2)
        maxN_2 = 0
        for i in range(length):
            array[i+2] = maxN_2 + nums[i]
            maxN_2 = max(maxN_2, array[i+1])
        return max(array[-1], array[-2])
# @lc code=end
n = [2,7,9,1,1,6]
sol = Solution()
print(sol.rob(n))

