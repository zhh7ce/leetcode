#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
from typing import List
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.dp = [0] * (n + 1)
        for i in range(n):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

sol = NumArray([-2,0,3,-5,2,-1])
print(sol.sumRange(0,2))
print(sol.sumRange(2,5))
print(sol.sumRange(0,5))
