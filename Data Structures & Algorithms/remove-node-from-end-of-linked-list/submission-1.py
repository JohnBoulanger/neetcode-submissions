# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        # get length of list
        while cur:
            cur = cur.next
            length += 1

        # skip first node
        if length == n:
            return head.next

        # otherwise jump over node length - n
        i = 0
        cur = head
        while i != (length - n - 1):
            cur = cur.next
            i += 1

        # skip it
        cur.next = cur.next.next
        return head