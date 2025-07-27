class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        # Remove consecutive duplicates
        arr = [nums[0]]
        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)

        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                res += 1  # hill
            elif arr[i - 1] > arr[i] < arr[i + 1]:
                res += 1  # valley

        return res