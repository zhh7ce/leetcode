#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
# @lc code=end

s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)