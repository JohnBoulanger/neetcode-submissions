# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists: return None

        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            res = dummy

            # combine lists in order while both not null
            while list1 and list2:
                if list1.val < list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next

                res = res.next
            # add remaining list thats not null
            res.next = list1 or list2
            return dummy.next

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # merge pairs together
                if i+1 < len(lists):
                    mergedLists.append(mergeTwoLists(lists[i], lists[i+1]))
                # wont have a pair, add it on its own
                else:
                    mergedLists.append(lists[i])
            # store the newly merged pairs in lists to use again until 1 list remains
            lists = mergedLists
                
        return lists[0]
