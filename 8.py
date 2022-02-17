#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        n = len(s)
        start = n-1
        end = 0
        neg = False
        for i in range(n):
            if s[i] != ' ':
                start = i
                break
        if s[start] == '-':
            neg = True
            start += 1
        elif s[start] == '+':
            start += 1
        for i in range(start, n):
            if s[i] not in number:
                end = i
                break
        else:
            end = n
        if end <= start:
            return 0
        ans = 0
        for i in range(start, end):
            ans *= 10
            ans += int(s[i])
        if neg:
            if ans > 2147483648:
                return -2147483648
            else:
                return -ans
        if ans > 2147483647:
            return 2147483647
        else:
            return ans
# @lc code=end

