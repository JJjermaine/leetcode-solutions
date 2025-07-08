class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, o, t = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
            elif nums[i] == 1:
                o += 1
            else:
                t += 1
        while nums:
            nums.pop()
        while z:
            nums.append(0)
            z -= 1
        while o:
            nums.append(1)
            o -= 1
        while t:
            nums.append(2)
            t -= 1
        