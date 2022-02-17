#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#

# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        nums.append(0)
        n = len(nums)
        left = 0
        right = k
        mid = k // 2
        odd = k % 2
        arr = nums[left:right]
        while right < n:
            arr.sort()
            if odd:
                ans.append(float(arr[mid]))
            else:
                ans.append((arr[mid]+arr[mid-1]) / 2)
            arr.remove(nums[left])
            arr.append(nums[right])
            left += 1
            right += 1
        return ans
# @lc code=end

