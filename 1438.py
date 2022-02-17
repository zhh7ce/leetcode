#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
from typing import List
# @lc code=start

class PriorityQueue:
    def __init__(self):
        super().__init__()
        self.arr = []
    
    def append(self, x):
        if not self.arr:
            self.arr.append(x)
        else:
            index = self.bsearch(x)
            self.arr.insert(index, x)
    
    def bsearch(self, x):
        start = 0
        end = len(self.arr)
        mid = (start + end) >> 1
        while start+1 < end:
            if self.arr[mid] == x:
                return mid
            elif self.arr[mid] < x:
                start = mid
            else:
                end = mid
            mid = (start + end) >> 1
        if self.arr[mid] < x:
            return end
        else:
            return start

    def remove(self, x):
        index = self.bsearch(x)
        self.arr.pop(index)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        window = PriorityQueue()
        window.append(nums[0])
        for val in nums[1:]:
            if window.arr[-1] - window.arr[0] > limit or window.arr[-1] - val > limit or val - window.arr[0] > limit:
                window.remove(nums[start])
                start += 1
            window.append(val)
        return len(nums) - start

# @lc code=end

nums = [1,5,6,7,8,10,6,5,6]
s = Solution()
print(s.longestSubarray(nums, 4))