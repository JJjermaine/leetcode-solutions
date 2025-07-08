class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        bob_res = []
        alice_res = []
        res = []

        while nums:
            bob_res.append(min(nums))
            nums.remove(min(nums))
            if nums:
                alice_res.append(min(nums))
                nums.remove(min(nums))

        while bob_res and alice_res:
            res.append(alice_res.pop(0))
            res.append(bob_res.pop(0))

        return res

