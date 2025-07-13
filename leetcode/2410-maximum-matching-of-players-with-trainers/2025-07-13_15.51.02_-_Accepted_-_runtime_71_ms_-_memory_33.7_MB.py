class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # greedy
        # greedily match the the highest that it can possibly match with
        players.sort()
        trainers.sort()
        pointer1 = len(players)-1
        pointer2 = len(trainers)-1
        if pointer1 == 0 and pointer2 == 0 and players[0] > trainers[0]:
            return 0
        res = 1
        while pointer1 > 0 and pointer2 > 0:
            while players[pointer1] > trainers[pointer2]:
                pointer1 -= 1

            res += 1
            pointer1 -= 1
            pointer2 -= 1

        return res