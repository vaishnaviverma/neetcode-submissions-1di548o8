class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans=set()
        for i in range(l-2):
            j=i+1
            k=l-1
            t=nums[i]
            while(j<k):
                curr_sum = nums[j]+nums[k]
                if curr_sum == -t:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif curr_sum>-t:
                    k-=1
                else:
                    j+=1
        
        act_ans = []
        for a in ans:
            act_ans.append(list(a))
        return act_ans
