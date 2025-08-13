
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # Initialize two pointers, 'low' at the beginning of the list and 'high' at the end.
#         low = 0
#         high = len(nums) - 1

#         # The loop continues as long as 'low' is less than or equal to 'high'.
#         # This condition ensures that the search space is not empty.
#         while low <= high:
#             # Calculate the middle index of the current search space.
#             # Using integer division '//' is crucial to get an integer index.
#             mid = (low + high) // 2

#             # Check if the middle element is the target.
#             if nums[mid] == target:
#                 # If it is, we've found the target and return its index.
#                 return mid
            
#             # If the middle element is less than the target,
#             # the target must be in the right half of the search space.
#             elif nums[mid] < target:
#                 # We discard the left half by moving the 'low' pointer to mid + 1.
#                 low = mid + 1
            
#             # If the middle element is greater than the target,
#             # the target must be in the left half of the search space.
#             else:
#                 # We discard the right half by moving the 'high' pointer to mid - 1.
#                 high = mid - 1
        
#         # If the loop finishes without finding the target, it means the target is not in the list.
#         # We return -1 as per the problem's requirements.
#         return -1



# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             if l == r and nums[l] == target:
#                 return l
            
#             mid = l + (r - l) // 2
#             midNum = nums[mid]
#             if midNum == target:
#                 return mid
#             elif midNum < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
                
#         return -1
      
