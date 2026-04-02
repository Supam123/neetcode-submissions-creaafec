class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s))+'#'+s
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        length = ""  
        while i < len(s):
            if(s[i] != "#"):
                length += s[i]
                i+=1
            else:
                l = int(length)
                word = s[i+1: i+l+1]
                output.append(word)
                i+=l+1
                length = ""
        return output


