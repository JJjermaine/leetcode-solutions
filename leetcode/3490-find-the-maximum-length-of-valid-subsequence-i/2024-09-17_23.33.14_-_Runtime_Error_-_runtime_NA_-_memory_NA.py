class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # greedy solution, go through all odd/even, odd/odd,  even/odd, even/even parities
        c = nums[0] % 2
        odd = 0
        even = 0
        both = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            // Check if the current number's parity matches the expected parity `c`.
            if num % 2 == c:
                // If yes, it means we are continuing a valid alternating pattern.
                both += 1
                // Flip the expected parity for the next number (0 becomes 1, 1 becomes 0).
                c = 1 - c
   
        return max(even, odd, both)