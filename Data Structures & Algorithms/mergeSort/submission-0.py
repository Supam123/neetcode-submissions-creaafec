# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        s=0
        e=len(pairs)-1
 

        def mSort(pairs,s,e):
            m = (s+e)//2
            if(e-s+1 <=1):
                return pairs # reached base case whcih measn the arr is sorted

            mSort(pairs,s,m) 
            mSort(pairs,m+1,e)

            merge(pairs,s,m,e)
        
        def merge(pairs,s,m,e):
            left = pairs[s:m+1]
            right = pairs[m+1:e+1]

            i,j,k=0,0,s
            while i < len(left) and j < len(right):
                if(left[i].key<=right[j].key):
                    pairs[k]=left[i]
                    i+=1
                else:
                    pairs[k]=right[j]
                    j+=1
                k+=1
            
            while i<len(left):
                pairs[k]=left[i]
                k+=1
                i+=1
            while j<len(right):
                pairs[k]=right[j]
                k+=1
                j+=1
        mSort(pairs, 0, len(pairs) - 1)  # call the recursive sort

        return pairs
            
            


        
