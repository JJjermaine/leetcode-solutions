class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        min_sum = float('inf')

        # current mountain
        for i in range(1, len(nums)-1):

            # traverse left side of mountain
            left_curr = float('inf')
            for j in range(i -1, -1, -1):
                if nums[i] > nums[j]:
                    left_curr = min(left_curr, nums[j])
                    

            # traverse right side of mountain
            right_curr = float('inf')
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    right_curr = min(right_curr, nums[j])

            
            # if there exists a smaller right and left side, make it our current minimum
            if right_curr !=  float('inf') and left_curr != float('inf'):
                curr_sum = right_curr + left_curr + nums[i]
                min_sum = min(min_sum, curr_sum)


        if min_sum == float('inf'):
            return -1

        return min_sum
        