class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        curr = 0
        next = 1
        back = len(nums) - 1

        a = []
        while a != 0:
            if nums[curr] + nums[next] == target:
                a.append(curr)
                a.append(next)
                break
            elif next == back: # if compared index reaches the end
                curr += 1
                next = curr + 1
            else:
                next += 1

        return a

            
                