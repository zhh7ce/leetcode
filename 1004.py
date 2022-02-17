#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from typing import List
# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = K
        used = K - sum(A[:K])
        n = len(A)
        while end < n:
            if A[end]:
                end += 1
            elif used < K:
                end += 1
                used += 1
            else:
                if not A[start]:
                    used -= 1
                if not A[end]:
                    used += 1
                start += 1
                end += 1
                while end < n and used > K:
                    if not A[start]:
                        used -= 1
                    if not A[end]:
                        used += 1
                    start += 1
                    end += 1
        return end - start
# @lc code=end

s = Solution()
A = [1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1]
K = 0
print(s.longestOnes(A, K))

