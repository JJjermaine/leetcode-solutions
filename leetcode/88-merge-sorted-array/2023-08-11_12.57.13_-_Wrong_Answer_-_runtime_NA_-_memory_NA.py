class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0
        while nums2_index < len(nums2):
            if nums2[nums2_index] <= nums1[nums1_index] or nums1[nums1_index] == 0:
                nums1.insert(nums1_index, nums2[nums2_index])
                nums1.pop()
                nums2_index += 1
            else:
                nums1_index += 1