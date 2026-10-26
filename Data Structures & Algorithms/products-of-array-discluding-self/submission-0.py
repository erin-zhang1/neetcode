class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # As this question can't use division, then consider left side of i * right side of i
        product_list = []
        for i in range(len(nums)):
            prefix_product = 1
            surfix_product = 1
            for pre_num in nums[:i]:
                prefix_product = prefix_product * pre_num
            for sur_num in nums[i+1:]:
                surfix_product *= sur_num
            
            product_list.append(prefix_product * surfix_product)
        return product_list