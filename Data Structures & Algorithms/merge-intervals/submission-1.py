class Solution:
    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        ints.sort()
        start = ints[0][0]
        end = ints[0][1]
        ans = []
        i = 0
        while i<len(ints):
            if ints[i][0]<=end:
                end = max(end, ints[i][1])
            else:
                ans.append([start, end])
                start = ints[i][0]
                end = ints[i][1]
            i+=1
        ans.append([start, end])
        return ans