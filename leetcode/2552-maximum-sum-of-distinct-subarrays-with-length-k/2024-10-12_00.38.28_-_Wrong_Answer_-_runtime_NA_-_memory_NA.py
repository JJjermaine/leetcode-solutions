class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # ans is my own & looked at hints
        count = {}
        # add first k elements to dictionary
        for i in range(k):
            count[nums[i]] = count.get(nums[i], 0) + 1

        res = 0
        for i in range(k, len(nums)):
            # if less than k amount of distinct elements, dont sum, just slide the window 
            if len(count) < k:
                # delete old side of window
                count[nums[i-k]] -= 1
                if count[nums[i-k]] == 0:
                    del count[nums[i-k]] 

                # add new side of window
                count[nums[i]] = count.get(nums[i], 0) + 1
            else:
                total_sum = sum(key * value for key, value in count.items())
                res = max(res, total_sum)
                
                # delete old side of window
                count[nums[i-k]] -= 1
                if count[nums[i-k]] == 0:
                    del count[nums[i-k]] 

                # add new side of window
                count[nums[i]] = count.get(nums[i], 0) + 1

        return res

            
            