class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            curr_count = {}
            res = []

            l = 0
            

            for r in range(len(nums)):
                if r < k:
                    if nums[r] not in curr_count:
                        curr_count[nums[r]] = 1
                    else:
                        curr_count[nums[r]] += 1

                else:
                    curr_max = max(curr_count)
                    res.append(curr_max)

                    if nums[r] not in curr_count:
                        curr_count[nums[r]] = 1
                    else:
                        curr_count[nums[r]] += 1
                    
                    curr_count[nums[l]] -= 1
                    if curr_count[nums[l]] == 0:
                        del curr_count[nums[l]]
                    l += 1

            curr_max = max(curr_count)
            res.append(curr_max)

            return res
        