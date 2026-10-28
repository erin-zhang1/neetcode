class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # quick search, remove duplicate nums
        start_points = []
        longest = 0

        for num in nums_set:
            if num -1 not in nums_set:
                start_points.append(num)
        
        for starter in start_points:
            length = 1
            cumulative_value = starter

            while cumulative_value +1 in nums_set:
                cumulative_value += 1
                length += 1

            longest = max(length,longest)
        
        return longest
            

        
        