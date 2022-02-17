#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#
from typing import List
# @lc code=start
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        self.array = [0] * N
        for i in range(N):
            self.array[i] = i+1 
        self.recursion(0, N)
        return self.array

    def recursion(self, start, end):
        # start is included
        # end is excluded
        if start + 2 >= end:
            return 
        odd = []
        even = []
        for i in range(start, end, 2):
            odd.append(self.array[i])
        for i in range(start+1, end, 2):
            even.append(self.array[i])
        m = len(odd)
        n = len(even)
        for i in range(m):
            self.array[start+i] = odd[i]
        for i in range(n):
            self.array[start+m+i] = even[i]
        self.recursion(start, start+m)
        self.recursion(start+m, end)
# @lc code=end

s = Solution()
print(s.beautifulArray(8))