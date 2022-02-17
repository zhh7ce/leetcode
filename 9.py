#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        while x > 0:
            arr.append(x % 10)
            x //= 10
        n = len(arr)
        for i in range(n//2):
            if arr[i] != arr[-1-i]:
                return False
        return True
# @lc code=end

