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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        ListNode* cur = head;
        ListNode* next = nullptr;
        ListNode* prev = nullptr;
        // find length of list
        int length = 0;
        while(cur) {
            cur = cur->next;
            length++;
        }
        
        // reverse second half of list round up
        int mid = (length + 1) / 2;
        int counter = 0;
        cur = head;
        // find midpoint node
        while (cur && counter < mid) {
            prev = cur;
            cur = cur->next;
            counter++;
        }

        // break off forward list from 2nd half
        prev->next = nullptr;
        prev = nullptr;
        // reversal of 2nd half
        while(cur) {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        ListNode* reverse = prev;
        ListNode* forward = head;
        ListNode* nextFwd = nullptr;
        ListNode* nextRev = nullptr;
        
        // merge lists
        while(forward && reverse) {
            // save nexts
            nextFwd = forward->next;
            nextRev = reverse->next;

            // update next nodes
            forward->next = reverse;
            reverse->next = nextFwd;

            // advance current nodes
            reverse = nextRev;
            forward = nextFwd;
        }
        return;
    }
};