class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ans not my own
        # use fast and slow pointers
        if len(nums) > 1:

            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow
            
        else:
            return -1

        