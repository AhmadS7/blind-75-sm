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


# from collections import deque

# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         # A deque to store indices of elements in the current window
#         dq = deque()
#         result = []

#         # Process the first k elements (initial window)
#         for i in range(k):
#             # Maintain a monotonically decreasing deque
#             # Pop smaller elements from the back
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()
#             dq.append(i)
        
#         # Add the maximum of the first window to the result
#         result.append(nums[dq[0]])

#         # Slide the window from the k-th element to the end
#         for i in range(k, len(nums)):
#             # Remove the index that is out of the current window from the front
#             if dq and dq[0] == i - k:
#                 dq.popleft()
            
#             # Maintain a monotonically decreasing deque
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()
            
#             # Add the new index to the back
#             dq.append(i)
            
#             # The maximum element's index is always at the front
#             result.append(nums[dq[0]])
            
#         return result
