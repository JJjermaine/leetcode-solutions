class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, 0
        res = []
        while l < n and r < n:
            while l < n:
                if nums[l] > 0:
                    res.append(nums[l])
                    l += 1
                    break
                l += 1
            
            while r < n:
                if nums[r] < 0:
                    res.append(nums[r])
                    r += 1
                    break
                r += 1
        return res