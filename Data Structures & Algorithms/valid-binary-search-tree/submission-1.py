# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def check(curr_node) -> tuple:
            nonlocal ans
            if not curr_node:
                return (1001, -1001)
            # left_data = check(curr_node.left)
            # right_data = check(curr_node.right)
            # minl = left_data[1] if len(left_data)>0 else 1001
            # maxl = right_data[0] if len(right_data)>0 else -1001
            left_min, left_max = check(curr_node.left)
            right_min, right_max = check(curr_node.right)

            if curr_node.val <= left_max or curr_node.val>=right_min:
                ans=False
            return (min(curr_node.val, left_min), max(curr_node.val, right_max))
        check(root)
        return ans
            
        