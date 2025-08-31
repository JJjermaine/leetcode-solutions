class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # needed  help
        sorted_nums = sorted(nums)
        # [1, 1, 1, 4, 5, 6]
        # [1, 6, 1, 4, 5, 1]
        mid = (len(nums) + 1) // 2
        l, r = mid - 1, len(nums) -1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[l]
                l -= 1
            else:
                nums[i] = sorted_nums[r]
                r -= 1


        