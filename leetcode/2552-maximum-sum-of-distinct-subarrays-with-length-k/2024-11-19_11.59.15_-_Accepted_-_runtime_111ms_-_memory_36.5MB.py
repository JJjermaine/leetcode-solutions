class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # ans is my own & looked at hints
        count = {}
        # add first k elements to dictionary
        current_sum = 0
        for i in range(k):
            count[nums[i]] = count.get(nums[i], 0) + 1
            current_sum += nums[i]

        res = 0
        for i in range(k, len(nums)):
            # just slide the window if less than k distinct elements
            if len(count) == k:
                res = max(res, current_sum)
            # delete old side of window
            count[nums[i-k]] -= 1
            current_sum -= nums[i-k]
            if count[nums[i-k]] == 0:
                del count[nums[i-k]] 

            # add new side of window
            count[nums[i]] = count.get(nums[i], 0) + 1
            current_sum += nums[i]

        # loop didnt sum the last k characters so perform here
        if len(count) == k:
            res = max(res, current_sum)

        return res

            
            