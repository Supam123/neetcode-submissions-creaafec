class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for word in strs:
            dna = [0] * 26
            for i in range(len(word)):
                code = ord(word[i]) - ord('a')
                dna[code] += 1
            key = tuple(dna)
            if(key not in dct):
                dct[key] = [word]
            else:
                dct[key].append(word)
        return list(dct.values())
     
               
                
        