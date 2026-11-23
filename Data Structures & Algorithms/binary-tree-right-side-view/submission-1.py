# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        # bfs on tree, right side is last node at each level
        def bfs(q):
            while q:
                # go through all nodes on layer
                n = len(q)
                for i in range(n):
                    node = q.popleft()
                    # if last node, save in res
                    if i == n - 1:
                        res.append(node.val)
                    # add left and right nodes if they exist
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        bfs(q)
        return res