class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        win_count = 0

        if k >= len(arr):
            for i in range(1, len(arr)):
                if arr[i] > current_winner:
                    current_winner = arr[i]

            return current_winner


        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                win_count += 1
            else:
                current_winner = arr[i]
                win_count = 1

            if win_count == k:
                return current_winner

        

        
        return current_winner