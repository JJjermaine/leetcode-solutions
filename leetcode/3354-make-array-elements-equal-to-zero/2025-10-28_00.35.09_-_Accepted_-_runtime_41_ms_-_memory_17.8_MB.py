class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # if left amount is equal to right amount
        # [1, 1, 3, 3, 6]
        # [6, 5, 5, 3, 3]
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]

        post = [0] * n
        post[-1] = nums[-1]
        for i in range(1, n):
            pref[i] = nums[i] + pref[i-1]

        for i in range(n-2,-1,-1):
            post[i] = nums[i] + post[i+1]
        
        res = 0
        for i in range(n):
            if nums[i] == 0 and pref[i] == post[i]-1:
                res += 1
            if nums[i] == 0 and pref[i]-1 == post[i]:
                res += 1
            if nums[i] == 0 and pref[i] == post[i]:
                res += 2
        return res