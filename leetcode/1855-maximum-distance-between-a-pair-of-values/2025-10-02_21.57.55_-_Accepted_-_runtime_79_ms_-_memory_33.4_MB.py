class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nonincreasing
        l = 0
        r = 0  
        res = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                res = max(r - l, res)
                r += 1
            else:
                l += 1
        return res
