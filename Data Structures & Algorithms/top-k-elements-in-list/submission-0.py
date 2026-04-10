class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            if num in data:
                data[num]+=1
            else:
                data[num]=1
        data = dict(sorted(data.items(), key=  lambda item: item[1], reverse=True))
        count = 0
        ans = []
        for item in data:
            if count==k:
                return ans
            ans.append(item)
            count+=1
        return ans