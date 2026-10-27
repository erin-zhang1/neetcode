from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            counts = Counter(word)
            key = tuple(sorted(counts.items()))

            mp[key].append(word)
        
        return list(mp.values())
        