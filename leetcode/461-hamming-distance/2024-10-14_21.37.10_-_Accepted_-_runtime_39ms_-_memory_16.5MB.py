class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        start_bit = bin(x)[2:]
        goal_bit = bin(y)[2:]

        len_diff = abs(len(start_bit) - len(goal_bit))
        if len(start_bit) > len(goal_bit):
            goal_bit = (len_diff * "0") + goal_bit
        else:
            start_bit = (len_diff * "0") + start_bit

        count = 0
        for s, g in zip(start_bit, goal_bit):
            if s != g:
                count += 1
        return count