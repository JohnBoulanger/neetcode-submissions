"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a map of nodes, if that node doesnt exist in the map, add it to the map
        # if we need to point to it again

        nodeMap = {}

        if not head: return None

        cur = head
        nodeMap[cur] = Node(cur.val)
        while cur:
            # get the nodes value 
            copy = nodeMap[cur]

            # get the nodes corresponding next and random nodes
            if not cur.next:
                copy.next = None
            elif cur.next in nodeMap:
                copy.next = nodeMap[cur.next]
            # if one doesnt exist, create a new node for it
            else:
                nodeMap[cur.next] = Node(cur.next.val)
                copy.next = nodeMap[cur.next]
            if not cur.random:
                copy.random = None
            elif cur.random in nodeMap:
                copy.random = nodeMap[cur.random]
            else:
                nodeMap[cur.random] = Node(cur.random.val)
                copy.random = nodeMap[cur.random]

            # move to next node in actual list
            cur = cur.next

        return nodeMap[head]



        