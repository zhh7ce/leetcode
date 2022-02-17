#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        ps = 0
        pg = 0
        while ps < len(s) and pg < len(g):
            if s[ps] >= g[pg]:
                ps += 1
                pg += 1
                count += 1
            elif s[-1] < g[pg]:
                break
            else:
                ps += 1
        return count

# @lc code=end
g=[1,2,3]
s=[1,3]
sol = Solution()
print(sol.findContentChildren(g, s))