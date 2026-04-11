# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        def travel(curr_node):
            nonlocal max_sum
            if not curr_node:
                return 0
            left_gain = travel(curr_node.left)
            right_gain = travel(curr_node.right)
            curr_sum = curr_node.val + left_gain + right_gain
            max_sum = max(max_sum, curr_sum)
            return max(0,curr_node.val + max(0,max(left_gain, right_gain)))
        travel(root)
        return max_sum
        