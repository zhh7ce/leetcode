#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for (x, y) in zip(s, t):
            arr.append(abs(ord(x) - ord(y)))
        left = 0
        right = 0
        cost = 0
        while right < len(s):
            if cost + arr[right] > maxCost:
                cost -= arr[left]
                cost += arr[right]
                left += 1
                right += 1
            else:
                cost += arr[right]
                right += 1
        return right-left
# @lc code=end

