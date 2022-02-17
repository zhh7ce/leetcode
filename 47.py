#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from typing import List
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        array = [[]]
        empty = [False] * n
        used = [empty]
        answer = []
        while array:
            a = array.pop()
            u = used.pop()
            if len(a) == n:
                answer.append(a)
            prev = float('inf')
            for i in range(n):
                if u[i]:
                    continue
                if prev == nums[i]:
                    continue
                else:
                    prev = nums[i]
                tmp = a.copy()
                tmp.append(nums[i])
                array.append(tmp)
                tmp = u.copy()
                tmp[i] = True
                used.append(tmp)
        return answer
# @lc code=end
s = Solution()
print(s.permuteUnique([1,2,3,4]))
