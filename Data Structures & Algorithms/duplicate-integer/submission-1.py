class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for n in nums:
            if n not in counts.keys():
                counts[n] = 0
            counts[n] += 1
        
        for i in counts.values():
            if i > 1:
                return True
        return False

        