class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        anslist = heapq.nlargest(k, nums)
        return anslist[-1]
        