class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r,w = 0,0,0
        length = len(chars)
        count =0
        while r < length:
            if chars[l] == chars[r]: # if they match
                r+=1 # increment r
                count+=1 # add 1 
            else:
                chars[w] = chars[l] # if they dont match write which is already written there
                w+=1 #move write up by 1 because TIME to wrtie the count
                if count > 1 :
                    s = str(count)
                    times = len(s)
                    for i in range(times):
                        chars[w] = s[i]
                        w+=1
                l = r
                count = 0
        chars[w] = chars[l]
        w += 1
        if count > 1:
            s = str(count)
            times = len(s)
            for i in range(times):
                chars[w] = s[i]
                w += 1
        return w  