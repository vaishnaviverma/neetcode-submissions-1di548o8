# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        max_val = root.val
        def dfs(curr_node, max_val):
            nonlocal count
            if not curr_node:
                return
            if curr_node.val>=max_val:
                count+=1
                max_val=curr_node.val
            dfs(curr_node.left, max_val)
            dfs(curr_node.right, max_val)
        dfs(root, max_val)
        return count