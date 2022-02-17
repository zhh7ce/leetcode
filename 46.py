#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        array = [[]]
        empty = [False] * n
        used = [empty]
        answer = []
        while array:
            a = array.pop()
            u = used.pop()
            if len(a) == n:
                answer.append(a)
            for i in range(n):
                if u[i]:
                    continue
                tmp = a.copy()
                tmp.append(nums[i])
                array.append(tmp)
                tmp = u.copy()
                tmp[i] = True
                used.append(tmp)
        return answer
# @lc code=end
s = Solution()
print(s.permute([]))
