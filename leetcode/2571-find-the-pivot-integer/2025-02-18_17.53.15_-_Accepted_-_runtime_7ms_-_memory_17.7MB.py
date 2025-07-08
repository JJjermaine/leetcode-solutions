class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
        
        prefix_sum = 0
        for x in range(1, n + 1):
            prefix_sum += x  # Sum from 1 to x
            suffix_sum = total_sum - prefix_sum + x  # Sum from x to n
            
            if prefix_sum == suffix_sum:
                return x  # Found the pivot integer
        
        return -1  # No pivot integer found


        