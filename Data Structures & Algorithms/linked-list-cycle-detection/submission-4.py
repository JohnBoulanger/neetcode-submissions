# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        # initalize fast pointer in front of slow
        slow = head
        fast = head.next

        # if the fast pointer == slow, it caught up because there was a cycle
        while slow and fast and fast.next:
            if slow == fast: return True
            # fast moves 2x as fast as slow
            slow = slow.next
            fast = fast.next.next

        return False
        