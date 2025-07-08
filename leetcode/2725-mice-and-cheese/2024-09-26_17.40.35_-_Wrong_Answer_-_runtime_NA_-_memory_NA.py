class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        mice1moves = 0
        mice2moves = 0
        res = 0
        pointer = 0
        while mice1moves < k and mice1moves < k or pointer < len(reward1) and pointer < len(reward2):
            if reward1[pointer] < reward2[pointer]:
                mice1moves += 1
                res += reward2[pointer]
            else:
                mice1moves += 1
                res += reward1[pointer]

            pointer += 1    


        return res


        