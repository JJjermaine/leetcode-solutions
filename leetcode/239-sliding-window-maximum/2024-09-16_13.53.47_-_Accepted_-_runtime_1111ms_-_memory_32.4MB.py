class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        deque_window = deque()  # Stores indices of the elements in the current window
        res = []

        for r in range(len(nums)):
            # Remove indices that are out of the current window
            if deque_window and deque_window[0] < r - k + 1:
                deque_window.popleft()

            # Remove elements smaller than the current element from the deque
            while deque_window and nums[deque_window[-1]] <= nums[r]:
                deque_window.pop()

            # Add current element's index to the deque
            deque_window.append(r)

            # The first element in the deque is the largest, add it to the result after window size is reached
            if r >= k - 1:
                res.append(nums[deque_window[0]])

        return res
        