from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            sort_arr = sorted(word)
            key = "".join(sort_arr)
            mp[key].append(word)

        return list(mp.values())
        