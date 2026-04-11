# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ Since BST is sorted in a manner that left-side
        nodes are less than the right-side nodes, and in-order traversal
        will fetch a sorted array.
        """
        nums = []

        def inorder_travel(curr_node):
            if not curr_node:
                return
            inorder_travel(curr_node.left)
            nums.append(curr_node.val)
            inorder_travel(curr_node.right)
        inorder_travel(root)
        return nums[k-1]