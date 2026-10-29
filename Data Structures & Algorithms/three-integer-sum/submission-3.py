class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue # skip current iteration

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    # skip duplicate l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return result
        

                
                    



