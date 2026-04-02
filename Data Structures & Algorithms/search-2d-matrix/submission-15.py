class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        bot,top = 0, len(matrix) - 1
        while bot <= top :
            mid = (bot+top) // 2
            if target < matrix[mid][0]:
                top = mid - 1
            elif target > matrix[mid][-1]:
                bot =  mid + 1
            else:
                l,r = 0,len(matrix[mid])
                while  l <= r:
                    m = (l+r)//2
                    if target < matrix[mid][m]:
                        r = m  - 1
                    elif target > matrix[mid][m]:
                        l = m  + 1
                    else:
                        return True
                return False
        return False


