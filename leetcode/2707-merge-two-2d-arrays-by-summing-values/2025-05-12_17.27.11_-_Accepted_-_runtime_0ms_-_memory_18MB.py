class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i in range(len(nums1)):
            id1, val1 = nums1[i]
            d[id1] += val1
        for i in range(len(nums2)):
            id2, val2 = nums2[i]
            d[id2] += val2
        res = []
        for k, v in d.items():
            res.append([k, v])
        res.sort()
        return res
        