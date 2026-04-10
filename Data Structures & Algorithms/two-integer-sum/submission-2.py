class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={nums[0]:0}
        for index, num in enumerate(nums):
            if target - num in dict1.keys() and index != dict1[target-num]:
                ans=[dict1[target-num],index]
                return ans
            else:
                dict1[num]=index

        