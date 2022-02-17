#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n:
            return n
        arr = [0] * 26
        maxCount = k
        start = 0
        end = max(k, 1)
        for i in s[start:end]:
            arr[ord(i)-65] += 1
        while end < n:
            if end-start-max(arr) < k or ord(s[end])-65 == arr.index(max(arr)):
                arr[ord(s[end])-65] += 1
                end += 1
                maxCount = max(maxCount, end-start)
            else:
                arr[ord(s[start])-65] -= 1
                # arr[ord(s[end])-65] += 1
                start += 1
                # end += 1
            print(start, end)
        return maxCount
# @lc code=end

