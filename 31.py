#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(-1, -n, -1):
            if nums[i] > nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                start = i
                end = -1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                break
        else:
            nums.reverse()
            
# @lc code=end

s = Solution()
num = [1,2,4,5,3]
s.nextPermutation(num)
print(num)

