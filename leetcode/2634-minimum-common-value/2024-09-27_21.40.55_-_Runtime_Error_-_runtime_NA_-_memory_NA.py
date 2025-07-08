class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        res = -1
        while p1 < len(nums1)-1 or p2 < len(nums2)-1:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res = nums1[p1]
                break

        return res
        