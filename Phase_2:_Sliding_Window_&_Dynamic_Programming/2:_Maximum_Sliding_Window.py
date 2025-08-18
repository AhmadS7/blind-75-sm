from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()       # Stores indices of useful elements
    result = []

    for i in range(len(nums)):
        # Remove indices outside the window
        while q and q[0] < i - k + 1:
            q.popleft()
        # Remove smaller values—they can't be max
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        # Start adding results once window is full
        if i >= k - 1:
            result.append(nums[q[0]])  # Front of queue is max
    return result
