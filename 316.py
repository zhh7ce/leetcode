#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        dic = dict()
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)
        print(dic)
        prev = -1
        for i in range(ord("a"),ord("z")+1):
            c = chr(i)
            if c in dic:
                if prev < max(dic[c]):
                    dic[c].sort()
                    for j in dic[c]:
                        if prev < j:
                            prev = j
                            dic[c] = j
                            break
                else:
                    dic[c] = min(dic[c])
        print(dic)
                    
# @lc code=end

