class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search for leftmost target and rightmost target
        # neede help
        def search(x):
            lo, hi = 0, len(nums)-1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid - 1           
            return lo

        lo = search(target)
        hi = search(target+1)-1

        if lo <= hi:
            return([lo, hi])
                
        return([-1, -1])
                