class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # contraints tell me o(n) solution only
        # observations
        # ints that are the same when reversed can be matched with another of the same kind
        # vice versa with ints that are not the same

        # looked at the hints

        
        res = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            string = str(nums[i])
            rev = string[::-1]
            intRev = int(rev)

            transformed = nums[i] - intRev
            d[transformed] += 1
            if d[transformed] > 1:
                res += d[transformed]-1

        return res % (10**9 + 7)
        