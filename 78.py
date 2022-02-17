#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        number = []
        index = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            index.append(i)
            number.append([nums[i]])
        while number:
            n = number.pop()
            i = index.pop()
            answer.append(n)
            for j in range(i+1, length):
                tmp = n.copy()
                tmp.append(nums[j])
                number.append(tmp)
                index.append(j)
        return answer
        
# @lc code=end

s = Solution()
print(s.subsets([]))
