#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(i, m):
                if nums1[i] < nums2[j]:
                    answer.append(nums2[j])
                    break
            else:
                answer.append(-1)
        return answer
# @lc code=end

nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))
