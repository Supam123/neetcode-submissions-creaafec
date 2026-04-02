class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        #counts are the arrays that  index represent chars and its
        # values there frequencyt

        count1 = [0] * 26
        count2 = [0] *26
        k = len(s1)
        for i in range(k):
            freq = ord(s1[i]) - ord('a')
            count1[freq] += 1
        
        while r < len(s2):

            freq = ord(s2[r]) - ord('a')
            count2[freq] += 1

            if(r-l+1) == k: # is my window size same as k
                if count1 == count2:
                    return True
                else:
                    count2[ord(s2[l])- ord('a')] -= 1
                    l+=1
            r+=1
        return False
        
