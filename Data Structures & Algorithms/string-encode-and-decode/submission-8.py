class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + '#' + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        length = ''
        while i < len(s):
            if(s[i]!="#"):
                length += s[i]
                i += 1
            else:
                l = int(length)
                word = s[i+1:i+l+1]
                output.append(word)
                i = i + l + 1
                length = ''
          
        return output



