class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [[math.sqrt(n[0]*n[0] + n[1]*n[1]),n[0],n[1]] for n in points]
        heapq.heapify(distance)
        ans_dist = heapq.nsmallest(k, distance)
        ans = [[n[1],n[2]] for n in ans_dist]
        return ans 
        