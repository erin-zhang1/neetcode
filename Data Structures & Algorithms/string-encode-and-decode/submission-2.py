class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list= []

        for string in strs:
            n = len(string)
            new_string = str(n) + '#' + string
            encoded_list.append(new_string)
        
        s = ''.join(encoded_list)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1 # find until j = #
            
            n = int(s[i:j]) # string’s length

            new_str = s[j+1:j+n+1]
            strs.append(new_str)

            i = j+n+1 # update i

        return strs
