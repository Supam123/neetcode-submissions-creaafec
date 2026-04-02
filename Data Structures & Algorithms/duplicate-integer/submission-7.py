class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] +=1
        for k,v in dct.items():
            if v > 1 :
                return True
        return False
