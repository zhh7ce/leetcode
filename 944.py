#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
from typing import List
# @lc code=start
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m = len(A)
        n = len(A[0])
        count = 0
        for i in range(n):
            for j in range(1, m):
                if ord(A[j][i]) < ord(A[j-1][i]):
                    count += 1
                    break
        return count
# @lc code=end

A = ["zyx", "wvu", "tsr"]
sol = Solution()
print(sol.minDeletionSize(A))