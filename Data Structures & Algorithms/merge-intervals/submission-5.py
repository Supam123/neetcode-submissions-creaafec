class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =  lambda x: x[0])
        merged_arr = [intervals[0]]
        for start,end in intervals[1:]:
            if start <= merged_arr[-1][1]:
                merged_arr[-1][1] = max(merged_arr[-1][1],end)
                
            else:
                merged_arr.append([start,end])
        return merged_arr
   

        