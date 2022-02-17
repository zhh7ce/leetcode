/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int map[128];
        for (int i = 0; i < 128; ++i) {
            map[i] = 0;
        }
        int start = 0;
        int end = 0;
        while (end < s.size()) {
            map[int(s[end])]++;
            end++;
            for (int i = 0; i < 128; ++i) {
                if (map[i] > 1) {
                    map[int(s[start])]--;
                    start++;
                    break;
                }
            }
        }
        return end - start;
    }
};
// @lc code=end

