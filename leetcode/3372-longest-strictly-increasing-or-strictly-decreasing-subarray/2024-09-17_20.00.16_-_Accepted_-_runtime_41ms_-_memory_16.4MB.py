class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_res = 1
        decreasing_res = 1
        max_len = 1


        for i in range(len(nums)-1):

            if nums[i] < nums[i+1]:
                increasing_res += 1
                decreasing_res = 1

            elif nums[i] > nums[i+1]:
                decreasing_res += 1
                increasing_res = 1
            
            else:
                increasing_res = 1
                decreasing_res = 1

            max_len = max(max_len, increasing_res, decreasing_res)

        return max_len

        