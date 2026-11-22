# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        # find length of the list first
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        # first (n - 1) // 2 are list 1
        mid = (n - 1) // 2
        # other half becomes reversed list
        
        cur = head
        prev = None
        i = 0
        while i <= mid:
            prev = cur
            cur = cur.next
            i += 1


        # at this point cur is the node after the first half, reverse it
        prev.next = None
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        r = prev
        f = head
        # insert r nodes between f nodes
        while r:
            fnxt = f.next
            rnxt = r.next
            f.next = r
            r.next = fnxt
            f = fnxt
            r = rnxt

        return