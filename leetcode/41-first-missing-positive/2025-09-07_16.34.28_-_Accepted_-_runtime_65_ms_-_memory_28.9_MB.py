class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # from the hints: 
        # simulate o(n) space and try applying to o(1) space
        # for o(n) space, add to hashmap and if curr in hashmap, += 1
        # o(2n) time to solve for o(1) space
        # 
        # d = Counter(nums)
        # curr = 1
        # while curr in d:
        #     curr += 1
        # return curr

        # from discussion: missing int must be in range [1..n]
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1  

            