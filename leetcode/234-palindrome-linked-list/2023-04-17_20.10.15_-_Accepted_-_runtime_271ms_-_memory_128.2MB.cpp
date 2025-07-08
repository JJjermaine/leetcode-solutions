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
#include <string>
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* current = head;
        vector<int> arr;
        while (current != NULL) {
            arr.push_back(current->val);
            current = current->next;
        }
        int len = arr.size();
        int front = 0;
        int back = len-1;
        while (front <= back) {
            if (arr[front] != arr[back])
                return false;
            front++;
            back--;
        }
        return true;
    }
};