# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        

        s=0 # so we have  starting index
        e=len(pairs)-1
        def qSort(pairs,s,e): # ending index will be length - 1 alasways 

            if(e-s+1<=1): # base case to stop recursion when there is only one item that is considered to be sorted

                return

            left=s # whatrever we call left will be he leftmost index = starting index 
            pivot =pairs[e] # whatever we call pivotwill be the rightmost elemnet                                                                          

            for i in range(s,e):
                if(pairs[i].key<pivot.key):
                    temp= pairs[left]
                    pairs[left]=pairs[i]
                    pairs[i]=temp
                    left+=1
            
            pairs[e]=pairs[left]  
            pairs[left]= pivot 


            qSort(pairs,s,left-1)
            qSort(pairs,left+1,e)
        qSort(pairs,s,e)
        return pairs