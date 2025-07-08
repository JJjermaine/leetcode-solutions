class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        max_val = 0
        res = 0
        for key, value in count.items():
            if value > max_val:
                res = key
                max_val = value

        return res

        