# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack, cur = [], root

        while stack or cur:
            # go as far left as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            # get leftmost node
            cur = stack.pop()
            # check if kth node
            k -= 1
            if k == 0:
                return cur.val
            # start searching right
            cur = cur.right

        return -1
