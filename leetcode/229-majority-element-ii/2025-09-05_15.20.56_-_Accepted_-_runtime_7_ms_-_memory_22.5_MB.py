class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        res = []
        for key, val in d.items():
            if val > len(nums) / 3:
                res.append(key)
        return res 