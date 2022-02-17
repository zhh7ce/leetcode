#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = 0
        p2 = n-1
        ptr = p0
        while ptr <= p2:
            print(nums, p0, p2, ptr, nums[ptr])
            if nums[ptr] == 0:
                for i in range(p0, n):
                    if nums[i] != 0:
                        p0 = i
                        break
                nums[ptr] = nums[p0]
                nums[p0] = 0
                for i in range(p0, n):
                    if nums[i] != 0:
                        p0 = i
                        break
                ptr = max(ptr, p0) + 1
            elif nums[ptr] == 2:
                for i in range(p2, -1, -1):
                    if nums[i] != 2:
                        p2 = i
                        break
                nums[ptr] = nums[p2]
                nums[p2] = 2
                for i in range(p2, -1, -1):
                    if nums[i] != 2:
                        p2 = i
                        break
            else:
                ptr += 1

# @lc code=end

nums = [2,0,2,1,1,0]
s = Solution()
s.sortColors(nums)
print(nums)