class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)
            if s1==s2:
                continue
            heapq.heappush(max_heap, -(s1-s2))
        if len(max_heap)==0:
            return 0
        return -heapq.heappop(max_heap)
        