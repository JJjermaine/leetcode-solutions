class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # [3, 5, 25, 26, 27, 30]
        # [30, 27, 25, 5, 4, 3]
        
        n = len(nums)
        dicPrefix = defaultdict(int)
        dicPostfix = defaultdict(int)
        curr = 0
        for i in range(n):
            curr += nums[i]
            dicPrefix[curr] = i # prefix[i], idx
        curr = 0
        for i in range(n-1,-1,-1):
            curr += nums[i]
            dicPostfix[curr] = i # postfix[i], idx

        minOp = float("inf")
        # check pref in respect to itself
        for k, v in dicPrefix.items():
            if k == x:
                minOp = min(minOp, v+1)
        # check postfix in respect to itsef
        for k, v in dicPostfix.items():
            if k == x:
                minOp = min(minOp, n-v)

        # check prefix in respect to postfix (works vice versa?)
        for k, v in dicPrefix.items():
            target = x - k
            if target in dicPostfix: # check in other
                prefRemoval = v + 1
                postRemoval = n - dicPostfix[target]
                minOp = min(minOp, prefRemoval + postRemoval)

        return -1 if minOp == float("inf") else minOp


