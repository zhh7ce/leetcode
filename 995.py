#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#
from typing import List
# @lc code=start
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = 0
        queue = []
        for index, val in enumerate(A[:n-K+1]):
            if queue and queue[0] == index-K:
                queue.pop(0)
            if not queue or not (len(queue) & 1):
                # which means that even or 0
                if not val:
                    queue.append(index)
                    ans += 1
            else:
                if val:
                    queue.append(index)
                    ans += 1
        for index, val in enumerate(A[n-K+1:]):
            if queue and queue[0] == index-K+n-K+1:
                queue.pop(0)
            if not queue or not (len(queue) & 1):
                # which means that even or 0
                if not val:
                    return -1
            else:
                if val:
                    return -1
        return ans

# @lc code=end
s = Solution()
A = [1,1,0]
print(s.minKBitFlips(A, 1))
