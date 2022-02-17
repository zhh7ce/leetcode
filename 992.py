#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
from typing import List
# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subProblem(A, K) - self.subProblem(A, K-1)

    def subProblem(self, A: List[int], K: int):
        n = len(A)
        start = 0
        end = 0
        ans = 0
        freq = [0] * (n+1)
        count = 0
        while end < n:
            i = A[end]
            if freq[i] == 0:
                count += 1
            freq[i] += 1
            end += 1
            while count > K:
                j = A[start]
                start += 1
                freq[j] -= 1
                if freq[j] == 0:
                    count -= 1
            ans += end - start
        return ans
    
# @lc code=end
s = Solution()
arr = [1,2,1,3,4]
print(s.subarraysWithKDistinct(arr, 3))

