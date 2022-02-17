#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        s1 = dict()
        s2 = dict()
        a1 = [0] * n
        a2 = [0] * n
        count = 0
        for i in range(n):
            if s[i] in s1:
                a1[i] = s1[s[i]]
            else:
                a1[i] = count
                s1[s[i]] = count
                count += 1
        count = 0
        for i in range(n):
            if t[i] in s2:
                a2[i] = s2[t[i]]
            else:
                a2[i] = count
                s2[t[i]] = count
                count += 1
        return a1 == a2

# @lc code=end

