class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in check:
                return [check[comp], i]
            else:
                check[nums[i]]=i