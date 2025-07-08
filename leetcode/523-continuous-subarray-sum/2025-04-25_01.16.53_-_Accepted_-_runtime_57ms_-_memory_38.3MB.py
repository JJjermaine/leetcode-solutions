class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_index = {0: -1}  # base case: mod 0 seen at index -1
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k if k != 0 else prefix_sum

            if mod in mod_index:
                if i - mod_index[mod] >= 2:
                    return True
            else:
                mod_index[mod] = i

        return False