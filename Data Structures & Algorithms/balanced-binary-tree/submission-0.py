# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def check(curr_node):
            nonlocal ans
            if curr_node is None:
                return 0
            left_h = check(curr_node.left)
            right_h = check(curr_node.right)
            if abs(left_h-right_h)>1:
                ans=False
            return 1 + max(left_h, right_h)
        check(root)
        return ans