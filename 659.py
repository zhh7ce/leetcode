#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = dict()
        for i in nums:
            # for j in dic.keys():
            #     if j < i-1:
            #         for k in dic[j]:
            #             if k < 3:
            #                 return False
            #     # del dic[j]
            if i-1 in dic:
                x = heapq.heappop(dic[i-1])
                if not dic[i-1]:
                    del dic[i-1]
                if i in dic:
                    heapq.heappush(dic[i], x+1)
                else:
                    dic[i] = [x+1]      
            else:
                if i in dic:
                    heapq.heappush(dic[i], 1)
                else:
                    dic[i] = [1]
        for i in dic.values():
            for j in i:
                if j < 3:
                    return False
        return True

# @lc code=end

nums = [1,2,3,3,4,5]
s = Solution()
print(s.isPossible(nums))
