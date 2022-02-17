#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        number = []
        for i in range(4):
            number.append(num % 10)
            num //= 10
        number.reverse()
        ans = ''
        arr = [{1:'M'}, {1:'C', 4:'CD', 5:'D', 9:'CM'},\
            {1:'X', 4:'XL', 5:'L', 9:'XC'}, {1:'I', 4:'IV', 5:'V', 9:'IX'}]
        for i in range(4):
            n = number[i]
            dic = arr[i]
            while n > 0:
                if n >= 9:
                    ans += dic[9]
                    n -= 9
                    continue
                if n >= 5:
                    ans += dic[5]
                    n -= 5
                    continue
                if n >= 4:
                    ans += dic[4]
                    n -= 4
                    continue
                if n >= 1:
                    ans += dic[1]
                    n -= 1
                    continue
        return ans
# @lc code=end

