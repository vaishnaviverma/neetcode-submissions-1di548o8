class Solution:
    def eraseOverlapIntervals(self, ints: List[List[int]]) -> int:
        ints.sort()
        pend = ints[0][1]
        ans = 0 
        for start, end in ints[1:]:
            if start<pend:
                ans = ans + 1
                pend = min(pend, end)
            else:
                pend = end
        return ans
