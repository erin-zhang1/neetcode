from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = Counter(list(s))
        counts_t = Counter(list(t))

        if counts_s == counts_t:
            return True
        return False