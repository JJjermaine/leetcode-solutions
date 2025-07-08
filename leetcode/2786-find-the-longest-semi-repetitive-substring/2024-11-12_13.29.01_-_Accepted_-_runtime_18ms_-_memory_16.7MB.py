class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Base case: if the length of the string is 1, the answer is 1
        if len(s) == 1:
            return 1

        count = 0  # Store the maximum length of semi-repetitive substring
        l = 0      # Left pointer of the sliding window
        duplicate_count = 0  # Track the number of consecutive duplicate pairs

        for r in range(1, len(s)):
            # Check if current character is the same as the previous one
            if s[r] == s[r - 1]:
                duplicate_count += 1
            
            # If we have more than one pair of consecutive duplicates, shift the window
            while duplicate_count > 1:
                # Move the left pointer up, check if we're removing a duplicate pair
                if s[l] == s[l + 1]:
                    duplicate_count -= 1
                l += 1
            
            # Update the maximum length of a valid semi-repetitive substring
            count = max(count, r - l + 1)
        
        return count
