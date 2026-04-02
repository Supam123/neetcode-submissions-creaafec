class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) < len(nums2):
            A,B = nums1,nums2
        else:
            A,B = nums2,nums1
        
        l = 0
        r = len(A) 
        total = (len(nums1)+ len(nums2))
        half = (len(nums1)+ len(nums2))//2
        while  l <= r:
            A_cut = (l+r)//2
            B_cut = half - A_cut

            A_leftmax = A[A_cut-1] if A_cut >0 else float('-inf')
            A_rightmin = A[A_cut] if A_cut < len(A) else float('+inf')
            B_leftmax = B[B_cut-1] if B_cut >0 else float('-inf')
            B_rightmin = B[B_cut] if B_cut < len(B) else float('+inf')

            if A_leftmax <= B_rightmin and B_leftmax <= A_rightmin:
                # split is valid 
                if total % 2 == 0:
                    median =  (max(A_leftmax,B_leftmax) + min(A_rightmin,B_rightmin))/2
                    return median
                else:
                    median = min(A_rightmin,B_rightmin)
                    return median
            else:
                if B_leftmax > A_rightmin:
                    l = A_cut + 1
                else:
                    r = A_cut - 1
            











        