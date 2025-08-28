def climbStairs(n):
    # This handles the base cases.
    # If there's 1 step, there's only 1 way (take 1 step).
    # If there are 2 steps, there are 2 ways (1+1 or 2).
    if n <= 2:
        return n
    
    # Initialize variables for the number of ways to reach the first two steps.
    # 'a' represents the number of ways to reach step (n-2).
    # 'b' represents the number of ways to reach step (n-1).
    a, b = 1, 2
    
    # Iterate from step 3 up to the final step 'n'.
    # This loop builds the solution from the bottom up.
    for _ in range(3, n + 1):
        # The number of ways to reach the current step is the sum of ways
        # to reach the previous two steps (n-1 and n-2).
        # We update our variables for the next iteration.
        # The old 'b' (ways to reach n-1) becomes the new 'a'.
        # The sum of old 'a' and old 'b' becomes the new 'b' (ways to reach the current step).
        a, b = b, a + b
        
    # After the loop finishes, 'b' holds the total number of ways to reach step 'n'.
    return b



# class Solution:
#     def climbStairs(self, n: int) -> int:
#     # Handle base cases
#         if n <= 1:
#             return 1
    
#         # Create a DP table to store the number of ways for each step
#         dp = [0] * (n + 1)
        
#         # Base cases for the DP table
#         dp[0] = 1
#         dp[1] = 1
    
#         # Build the solution from the bottom up
#         for i in range(2, n + 1):
#             # The number of ways to reach step i is the sum of ways to reach
#             # step i-1 and step i-2
#             dp[i] = dp[i - 1] + dp[i - 2]
            
#         return dp[n]
