class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        idx = 0
        res = 0

        while True:
            if idx < len(arr) and curr == arr[idx]:
                idx += 1
            else:
                res += 1
                if res == k:    # return the k-th missing number
                    return curr
            curr += 1
