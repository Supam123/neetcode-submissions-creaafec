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
        # my question to u is why are we not doing it like insert intervale
        # like why are we not doing min of starts and max of ends 
        # and why are we not doing if it start ebfore or after oh well
        # cuz we are not intersting anythign ehre. 
        # a interval overlaps with another interval in a sorted list
        # if it starts before the last interval finishes 
        #hence the last interval need to expand to the max of itsefl odr the new end 
   

        