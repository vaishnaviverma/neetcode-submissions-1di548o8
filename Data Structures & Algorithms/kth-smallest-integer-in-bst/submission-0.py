# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        heapq.heapify(nums)
        def dfs(curr_node):
            nonlocal nums
            if not curr_node:
                return
            heapq.heappush(nums, curr_node.val)
            dfs(curr_node.left)
            dfs(curr_node.right)
        dfs(root)
        mini = heapq.nsmallest(k, nums)
        return mini[k-1]