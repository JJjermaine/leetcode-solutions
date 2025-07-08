class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        longest_mountain = 0
        i = 1
        
        while i < len(arr) - 1:
            # Check if current position could be a peak
            is_peak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
            
            if not is_peak:
                i += 1
                continue
            
            # Extend left side of the mountain
            left = i - 1
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            
            # Extend right side of the mountain
            right = i + 1
            while right < len(arr) - 1 and arr[right] > arr[right+1]:
                right += 1
            
            # Calculate current mountain length
            mountain_length = right - left + 1
            longest_mountain = max(longest_mountain, mountain_length)
            
            # Move to the end of current mountain
            i = right + 1
        
        return longest_mountain