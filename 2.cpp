/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        ListNode* tmp = ans;
        int val = 0;
        int plus = 0;
        int sum = 0;
        while (l1 or l2 or plus) {
            sum = 0;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            sum += plus;
            if (sum > 9) {
                val = sum - 10;
                plus = 1;
            } else {
                val = sum;
                plus = 0;
            }
            ListNode* n = new ListNode(val);
            tmp->next = n;
            tmp = n;
        }
        return ans->next;
    }
};
// @lc code=end
