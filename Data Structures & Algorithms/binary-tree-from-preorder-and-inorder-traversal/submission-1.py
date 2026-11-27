# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # map to find index of value in inorder
        idx = {val: i for i, val in enumerate(inorder)}
        p = 0

        def build(l, r):
            nonlocal p
            if l > r:
                return None
            # create root for subtree
            root = TreeNode(preorder[p])
            # increment because we search preorder
            p += 1
            # everything left of m is left subtree, everything right is right subtree
            m = idx[root.val]
            # search left subtree and build its tree first, then right because thats the order preorder visits them
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        root = build(0, len(preorder) - 1)
        return root
