class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for words in strs:
            dna = [0] * 26
            for i in range(len(words)):
                code = ord(words[i]) - ord('a')
                dna[code] += 1
            
            key = tuple(dna)
            if key in dct:
                dct[key].append(words)
            else:
                dct[key] = [words]
        return list(dct.values())

        