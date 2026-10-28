class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        surfix = 1

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            output[i] *= surfix
            surfix *= nums[i]
        
        return output
        