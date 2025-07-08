class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) == 2: return True
        operation = abs(arr[0] - arr[1])
        for i in range(1, len(arr)):
            if abs(arr[i-1] - arr[i]) != operation:
                return False

        return True
        