class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_seen = {}  # Dictionary to store the last day each task was performed
        current_day = 0  # The current day or time counter

        for task in tasks:
            # If the task has been done before and the cooldown period hasn't passed
            if task in last_seen and current_day - last_seen[task] <= space:
                # Skip days until the cooldown period is over
                current_day = last_seen[task] + space + 1
            
            # Execute the task on the current day
            last_seen[task] = current_day
            # Move to the next day
            current_day += 1

        return current_day  # Return the total number of days needed to complete all tasks