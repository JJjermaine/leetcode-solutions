class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # looked at solution

        n = len(nums) // 3

        # prefix min via min heap
        pref_min = [sum(nums[:n])]
        curr_min = sum(nums[:n])
        pre_hp = [-num for num in nums[:n]]
        heapq.heapify(pre_hp)
        for i in range(n, n * 2):
            curr_pop = -heapq.heappop(pre_hp)
            curr_min -= curr_pop
            curr_min += min(curr_pop, nums[i])
            pref_min.append(curr_min)
            heapq.heappush(pre_hp, -min(curr_pop, nums[i]))

        # suffix max via max heap
        suff_max = [sum(nums[2*n:])]
        curr_max = sum(nums[2*n:])
        suff_hp = [num for num in nums[2*n:]]
        heapq.heapify(suff_max)
        for i in range(2*n-1, n-1, -1):
            curr_pop = heapq.heappop(suff_hp)
            curr_max -= curr_pop
            curr_max += max(curr_pop, nums[i])
            suff_max.append(curr_max)
            heapq.heappush(suff_hp, max(curr_pop, nums[i]))
        suff_max = suff_max[::-1]

        res = float("inf")
        for i in range(len(pref_min)):
            res = min(res, pref_min[i] - suff_max[i])

        return res
        