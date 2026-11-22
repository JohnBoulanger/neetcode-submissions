# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        
        q = deque([root])
        res = []

        while q:
            level = []
            # search one level at a time,
            for i in range(len(q)):
                # remove node from front of queue (FIFO)
                node = q.popleft()
                # add it to the level
                level.append(node.val)

                # add its children which will be searched in the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

