class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) % 2 == 0:
            behind = 1
        else:
            behind = 2
        l = 0
        r = 1
        count = 1
        sum = nums[l] + nums[r]

        while r < len(nums)-behind:
            l += 2
            r += 2
            if sum != nums[l] + nums[r]:
                break
            else:
                sum = nums[l] + nums[r]
                count += 1
            

        return count
            
            
