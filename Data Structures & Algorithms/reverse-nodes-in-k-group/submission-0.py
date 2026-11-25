# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseList(head, k):
            if not head: return None, None, None

            cur = head
            prev = None
            count = 0
            # only reverse if remaining list has k nodes
            while cur and count < k:
                cur = cur.next
                count += 1

            if count != k:
                return head, None, None

            cur = head
            prev = None
            count = 0
            while cur and count < k:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt
                count += 1

            # returns head of rev list, tail of rev list, and node in front of rev list
            return prev, head, cur

        # reverse initial k nodes, save the head in head.
        cur = head
        head, revTail, cur = reverseList(cur, k)
        prevTail = revTail
        while cur:
            # reverse next group of k nodes
            revHead, revTail, cur = reverseList(cur, k)
            # assign previous tail to newly reversed head
            prevTail.next = revHead
            # update previous tail
            prevTail = revTail
            
        # return the head
        return head
                