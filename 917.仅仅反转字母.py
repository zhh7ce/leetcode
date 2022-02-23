#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        start = 0
        end = n-1
        while start < end:
            number = ord(arr[start])
            if  number < 65 or number > 122 or (number > 90 and number < 97):
                start += 1
                continue
            number = ord(arr[end])
            if number < 65 or number > 122 or (number > 90 and number < 97):
                end -= 1
                continue
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -=1
        return ''.join(arr)
# @lc code=end

