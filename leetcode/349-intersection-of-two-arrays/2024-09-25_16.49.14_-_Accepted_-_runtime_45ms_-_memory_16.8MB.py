class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()

        for num in nums1:
            set1.add(num)

        for num in nums2:
            set2.add(num)

        res = []
        for num in set1:
            if num in set2:
                res.append(num)

        return res

        