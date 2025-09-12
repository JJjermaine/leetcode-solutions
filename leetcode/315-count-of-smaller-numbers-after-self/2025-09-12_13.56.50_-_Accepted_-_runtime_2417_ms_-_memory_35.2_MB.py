class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # naive solution is n^2 where you loop through each and loop through again to 
        # find number of smaller elements
        # got help from solutions

        arr = sorted(nums)
        res = []
        n = len(nums)

        for i in range(n):
            # binary search for each leftmost nums[i] in sorted array
            lo = 0
            hi = len(arr)-1
            while lo <= hi:
                mid = (hi + lo) // 2
                if arr[mid] >= nums[i]:
                    pos = mid      # move left, keep candidate
                    hi = mid - 1
                else:
                    lo = mid + 1

            res.append(pos)
            del arr[pos]
                    
        return res
                    