class Solution:

    def encode(self, strs: List[str]) -> str:
        revised_strs = []
        for i in range(len(strs)):
            n = len(strs[i])
            r = str(n) + "#" + strs[i]
            revised_strs.append(r)
        
        return "".join(revised_strs)



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        
        return res
