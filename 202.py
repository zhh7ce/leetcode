#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            if n == 1:
                return True
            if n in s:
                return False
            else:
                s.add(n)
            arr = list(str(n))
            n = 0
            for i in arr:
                n += int(i) * int(i)

# @lc code=end

s = Solution()
print(s.isHappy(123))

