class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr,target):
            left =0
            right= len(arr)-1
            while(left<=right):
                mid= (left+right)//2
                if(target< arr[mid]):
                    right = mid-1
                elif(target>arr[mid]):
                    left = mid+1
                else:
                    return True
            return False

        leftM = 0
        rightM = len(matrix)-1
        while (leftM<=rightM ):
            mid = (leftM+rightM)//2

            # if(target>=matrix[mid][0] and target <= matrix[mid][-1]):
            #     #this is where we execute Binary search
            #     return binarySearch(matrix[mid],target)
            
            if(target<matrix[mid][0]):
                rightM = mid-1
            
            elif(target>matrix[mid][-1]):
                leftM = mid+1
            else:
                return binarySearch(matrix[mid],target)



        return False

        



        