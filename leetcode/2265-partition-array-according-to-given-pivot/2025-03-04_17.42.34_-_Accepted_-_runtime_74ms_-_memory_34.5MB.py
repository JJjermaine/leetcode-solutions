class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
       # lessthanCount = 0
        #for num in nums: 
         #   if num < pivot:
          #      lessthanCount += 1
        
        # naive solution?
        res = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == pivot:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i] > pivot:
                res.append(nums[i])
        return res

        