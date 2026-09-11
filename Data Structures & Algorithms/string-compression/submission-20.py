class Solution:
    def compress(self, chars: List[str]) -> int:
        
        read = 0
        length = len(chars)
        write = 0
        while read< length:
            curr =  chars[read]
            count = 0
          
            while read < length and chars[read] == curr:
                read += 1
                count +=1 
            chars[write] = curr
            write += 1
            if count > 1:
                count = str(count)
                for i in range(len(count)):
                    chars[write] = count[i]
                    write += 1
        return write
      
            

        