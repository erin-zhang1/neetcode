from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k_list = counts.most_common(k)
        return [num for num,_ in top_k_list]