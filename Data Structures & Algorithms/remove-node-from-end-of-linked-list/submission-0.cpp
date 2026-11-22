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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur = head;
        ListNode* prev = nullptr;
        int counter = 0;
        int length = 0;
        // get length of list
        while(cur) {
            cur = cur->next;
            length++;
        }
        // edge case
        if (n == length) return head->next;

        // length - counter = dist from end
        cur = head;
        while(cur) {
            // hit nth node from end, remove it
            if ((length - counter) == n) {
                prev->next = cur->next;
                break;
            }
            // otherwise keep looking
            prev = cur;
            cur = cur->next;
            counter++;
        }
        return head;
    }
};
