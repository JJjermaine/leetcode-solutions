class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #customers.sort()
        total_wait = 0
        curr_wait = 0

        for arrival, time in customers:
            if curr_wait >= arrival:
                curr_wait += time
            else:
                curr_wait = arrival
                curr_wait += time

            total_wait += curr_wait - arrival
        return total_wait / len(customers)


