class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        incr = 0
        curr = []
        smallest = nums[0]
        res = []
        for i in range(n):
            if incr == 3:
                incr = 0
                res.append(curr)
                curr = []
                smallest = nums[i]
                
                print(curr)

            if nums[i] - smallest > k:
                return []
            curr.append(nums[i])
            incr += 1

        if incr == 3:
            incr = 0
            res.append(curr)
            curr = []
            smallest = nums[i]
        return res

