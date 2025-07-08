class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # simulate deleting the lowest freq chars and simulate deleting the highest freq chars
        d = Counter(word)
        sorted_items = sorted(d.items(), key=lambda item: item[1])
        smallest = float("inf")
        delete = 0
        # simulate deleting lowest freq chars
        for i in range(len(sorted_items)):
            curr = abs(sorted_items[i][1] - sorted_items[-1][1])
            if curr <= k:
                smallest = delete# min(smallest, delete)
                break
            delete += sorted_items[i][1]
        delete_sum = 0
        delete = 0
        for i in range(len(sorted_items)):
            delete = delete_sum
            amount = 1
            pointer = len(sorted_items) - 2
            # simulate decrementing highest freq chars without each of the front
            highest_freq = sorted_items[-1][1]
            
            while highest_freq > 0:
                curr = abs(sorted_items[i][1] - highest_freq)
                if curr <= k:
                    smallest = min(smallest, delete)
                    break
                
                while sorted_items[pointer][1] >= highest_freq and pointer > i:
                    amount += 1
                    pointer -= 1
                highest_freq -= 1
                delete += 1 * amount
            delete_sum += sorted_items[i][1]

        return smallest