# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        cur = head
        nxt = cur.next
        prev = None
        # iterate through entire linked list (next is none for last node)
        while nxt is not None:
            # point the current nodes next to its previous, move all of them forward one
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next
        # point the last nodes next to its previous
        cur.next = prev
        return cur
