class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # sliding window
        n = len(nums)
        res = []
        satisfy = 1
        for i in range(1, n):
            if nums[i-1] + 1 == nums[i]:
                satisfy += 1
                if satisfy > k:
                    satisfy -= 1
            else:
                satisfy -= 1
                if satisfy == 0:
                    satisfy = 1
            if i+1 >= k:
                if satisfy == k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res
        

