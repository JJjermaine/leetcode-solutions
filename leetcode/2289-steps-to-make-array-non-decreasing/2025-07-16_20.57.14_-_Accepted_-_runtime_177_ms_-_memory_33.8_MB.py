class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # had to look at sol 
        # stack
        stack = []  # each element is a tuple (num, steps to remove)
        max_steps = 0

        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
            else:
                steps = 0
            max_steps = max(max_steps, steps)
            stack.append((num, steps))
        return max_steps
