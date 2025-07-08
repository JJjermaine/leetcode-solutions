class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        operations = 0

        for key, value in count.items():
            if value % 3 == 0:
                operations += value // 3
            elif value % 2 == 0:
                operations += value // 2
            else:
                return -1

        return operations
        