class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        # monotonic stack
        while left+1 < len(arr) and arr[left] <= arr[left+1]: 
            left+=1

        if left == len(arr) - 1:
            return 0

        stack = []
        for i in range(len(arr)-1, -1, -1):
            stack.append(i)
            if arr[i-1] > arr[i]:
                break

        remove = min(len(arr) - left - 1, stack[-1])
        for i in range(0, left+1):
            while stack and arr[i] > arr[stack[-1]]: 
                stack.pop()
            if stack:  
                remove = min(remove, stack[-1] - i - 1)
                
        return remove