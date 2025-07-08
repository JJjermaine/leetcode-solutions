class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window // ans not my own
        left = 0
        total_pairs = 0
        count_map = defaultdict(int)
        ans = 0
        n = len(nums)

        for right in range(n):
            total_pairs += count_map[nums[right]]
            count_map[nums[right]] += 1

            while total_pairs >= k:
                ans += n - right
                count_map[nums[left]] -= 1
                total_pairs -= count_map[nums[left]]
                left += 1

        return ans