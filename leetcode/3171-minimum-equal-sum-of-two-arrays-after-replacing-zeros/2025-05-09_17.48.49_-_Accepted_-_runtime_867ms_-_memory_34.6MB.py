class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # example 1
        # [3,2,0,1,0] -> sum of 6 with 2 zeros to fill in, [3] or [2,4] on each 0 to sum to 12
        # [6,5,0] -> sum of 11 with 1 zero to fill in, [1] on each 0
        # 
        # we want minimum sum, so can greedily assign 1 to lowest 0?

        sum1, zeros1, sum2, zeros2 = 0, 0, 0, 0
        for i in range(len(nums1)):
            sum1 += nums1[i]
            if nums1[i] == 0:
                zeros1 += 1
        for i in range(len(nums2)):
            sum2 += nums2[i]
            if nums2[i] == 0:
                zeros2 += 1

        smallest1 = sum1 + zeros1
        smallest2 = sum2 + zeros2

        if smallest1 != smallest2 and (smallest2 > smallest1 and zeros1 == 0) or (smallest1 > smallest2 and zeros2 == 0):
            return -1

        if smallest1 > smallest2:
            return smallest1

        else:
            return smallest2
