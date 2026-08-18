class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for n in  nums :
            if n not  in dct :
                dct[n] =1
            else:
                dct[n]+=1
        
        for k,v in dct.items():
            if v > 1 :
                return True
        
        return False
                
         