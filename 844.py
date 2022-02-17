#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        for i in S:
            if i == '#':
                if s:
                    s.pop()
                continue
            s.append(i)
        t = []
        for i in T:
            if i == '#':
                if t:
                    t.pop()
                continue
            t.append(i)
        if s != t:
            return False
        return True
# @lc code=end

sol = Solution()
print(sol.backspaceCompare("y#fo##f","y#f#o##f"))
