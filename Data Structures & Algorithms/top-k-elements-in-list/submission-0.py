class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for integer in nums:
            if integer not in counts:
                counts[integer] = 0
            counts[integer] += 1

        sorted_counts = dict(sorted(counts.items(), key = lambda count: count[1], reverse = True))
        result = []
        for i in sorted_counts.keys():
            result.append(i)
        return result[0:k]
