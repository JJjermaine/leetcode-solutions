class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # becomes house robber problem once converted to a dictionary
        nums.sort()
        d = defaultdict(int)

        for num in nums:
            d[num] += num

        items_list = list(d.items())
        n = len(items_list)
        dp = [0] * n
        i = 0

        for i in range(n):
            if items_list[i][0] == (items_list[i-1][0] + 1):
                dp[i] = max(items_list[i][1] + dp[i-2], dp[i-1])
            else:
                dp[i] = dp[i-1] + items_list[i][1]


        return dp[-1]