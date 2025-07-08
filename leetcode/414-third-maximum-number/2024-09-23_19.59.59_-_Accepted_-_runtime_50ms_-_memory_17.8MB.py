class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        if len(count) < 3:
            return max(count.keys()) # return max if third max doesnt exist

        count = sorted(count.keys(), reverse = True) # sort by keys

        return count[2] # third distinct max num

        
        