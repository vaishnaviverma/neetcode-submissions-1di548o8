class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxheap = nums
        heapq.heapify_max(self.maxheap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.maxheap, val)
        ans = heapq.nlargest(self.k, self.maxheap)
        return ans[-1]
