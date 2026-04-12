# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = -101
        minv = min(p.val, q.val)
        maxv = max(p.val, q.val)
        def check(curr_node):
            nonlocal ans
            if not curr_node:
                return
            cval = curr_node.val
            if minv<cval and maxv<cval:
                check(curr_node.left)
            elif minv>cval and maxv>cval:
                check(curr_node.right)
            else:
                ans=curr_node
        check(root)
        return ans