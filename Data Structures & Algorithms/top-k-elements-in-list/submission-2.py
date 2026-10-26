from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        tuples = counts.most_common(k)

        result = []

        for vals, i in tuples:
            result.append(vals)
        return result