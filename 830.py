#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
from typing import List
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if not s:
            return []
        n = len(s)
        element = s[0]
        start = 0
        length = 0
        ans = []
        for i in range(n):
            if element != s[i]:
                if length > 2:
                    ans.append([start, i-1])
                start = i
                element = s[i]
                length = 1
            else:
                length += 1
        if length > 2:
            ans.append([start, n-1])
        return ans

# @lc code=end

s = Solution()
print(s.largeGroupPositions('aaa'))