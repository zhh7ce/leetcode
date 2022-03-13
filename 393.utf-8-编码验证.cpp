/*
 * @lc app=leetcode.cn id=393 lang=cpp
 *
 * [393] UTF-8 编码验证
 */
#include<vector>
using namespace std;

// @lc code=start
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int extend = 0;
        for (auto i: data) {
            if (extend > 0) {
                if (i < 128 || i >= 192) return false;
                extend--;
            } else if (i < 128) {
                continue;
            } else if (i < 192) {
                return false;
            } else if (i < 224) {
                extend = 1;
            } else if (i < 240) {
                extend = 2;
            } else if (i < 248) {
                extend = 3;
            } else {
                return false;
            }
        }
        return extend == 0;
    }
};
// @lc code=end

