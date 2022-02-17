#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
from typing import List
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = len(nums)
        nums.sort()
        answer = [[]]
        stack = []
        index = []
        stack.append([nums[0]])
        index.append(1)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            stack.append([nums[i]])
            index.append(i+1)
        while stack:
            s = stack.pop()
            i = index.pop()
            answer.append(s)
            if i < n:
                tmp = s.copy()
                tmp.append(nums[i])
                stack.append(tmp)
                index.append(i+1)
            for j in range(i+1, n):
                if nums[j] == nums[j-1]:
                    continue
                tmp = s.copy()
                tmp.append(nums[j])
                stack.append(tmp)
                index.append(j+1)
        return answer
# @lc code=end

s = Solution()
print(s.subsetsWithDup([]))
