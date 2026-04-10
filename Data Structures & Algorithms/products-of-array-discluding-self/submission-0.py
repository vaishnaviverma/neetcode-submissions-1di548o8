class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        count_zero = 0
        for num in nums:
            if num!=0:
                total_prod*=num
            else:
                count_zero+=1
        ans = [0] * len(nums)
        if count_zero>1:
            return ans
        elif count_zero==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    ans[i]=total_prod
        else:
            for i in range(len(nums)):
                ans[i] = int(total_prod/nums[i])
        return ans

        