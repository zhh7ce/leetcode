#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        singal = 0
        length = 1
        prev = arr[0]
        maxCount = 1
        for now in arr[1:]:
            newSig = 0
            if now > prev:
                newSig = 1
            elif now < prev:
                newSig = -1
            if newSig:
                if singal != newSig:
                    length += 1
                    maxCount = max(maxCount, length)
                else:
                    length = 2
            else:
                length = 1
            singal = newSig
            prev = now
        return maxCount

# @lc code=end

