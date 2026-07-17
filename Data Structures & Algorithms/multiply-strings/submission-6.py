class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"
        nums1,nums2 = nums1[::-1],nums2[::-1]
        res = [0] * (len(nums1) + len(nums2)) 
        for i1 in range(len(nums1)):
            for i2 in range(len(nums2)):
                digit =  int(nums1[i1]) * int(nums2[i2])
                res[i1+i2] += digit
                res[i1+i2+1] +=  res[i1+i2] // 10
                res[i1+i2] =  res[i1+i2] %10
        res = res[::-1]
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        return ''.join(str(d) for d in res[start:])