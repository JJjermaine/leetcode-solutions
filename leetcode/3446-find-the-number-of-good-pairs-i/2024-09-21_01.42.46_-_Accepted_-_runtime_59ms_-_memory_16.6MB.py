class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                check = nums1[i] / (nums2[j] * k)
                if int(check) == check:
                    count += 1 

        return count
        