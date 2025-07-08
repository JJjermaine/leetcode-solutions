class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        curr_max = 0

        for i in range(1, len(nums)-1):

            # traverse left side to get max value
            left_max = 0
            for j in range(i-1,-1,-1):
                left_max = max(left_max, nums[j])


            # traverse right side to get max value
            right_max = 0
            for j in range(i+1, len(nums)):
                right_max = max(right_max, nums[j])
            
            curr_val = (left_max - nums[i]) * right_max

            curr_max = max(curr_max, curr_val)
            
        if sum(nums) <= 0:
            return 0

        return curr_max

        