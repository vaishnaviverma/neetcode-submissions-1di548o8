class Solution:
    def is_possible(self, piles, h, k):
        time = 0
        for i in piles:
            time+= math.ceil(i/k)
        if time<=h:
            return True
        else:
            return False
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        l = 1
        h = max(piles)
        ans = h
        while(l<=h):
            mid = l+int((h-l)/2)
            if self.is_possible(piles, hours, mid):
                h=mid-1
                ans = min(ans,mid)
            else:
                l=mid+1
        return ans
        