
def lengthOfLongestSubstring(s):
    char_set = set()      # To store unique characters
    left = 0              # Left pointer of the window
    max_len = 0           # Result

    for right in range(len(s)):  # Right pointer moves forward
        while s[right] in char_set:  # If duplicate found
            char_set.remove(s[left]) # Shrink window from left
            left += 1
        char_set.add(s[right])       # Add new character
        max_len = max(max_len, right - left + 1)  # Update result
    return max_len

# def lengthOfLongestSubstring(s):
#     # A hash set (or 'char_set') is a perfect data structure for this problem.
#     # It provides O(1) average time complexity for adding, removing, and checking for an element's existence.
#     # We use it to store the unique characters within our current window.
#     char_set = set()
    
#     # The 'left' pointer marks the beginning of our sliding window.
#     left = 0
    
#     # 'max_len' stores the maximum length of a valid substring found so far.
#     # This is the value we'll return at the end.
#     max_len = 0

#     # The 'right' pointer iterates through the string, expanding the window one character at a time.
#     for right in range(len(s)):
#         # This is the core of the sliding window technique.
#         # If the character at the 'right' pointer is already in our set, it means we have a duplicate.
#         # The 'while' loop handles the "shrinking" of the window.
#         while s[right] in char_set:
#             # We remove the character at the 'left' pointer from our set.
#             char_set.remove(s[left])
            
#             # Then we move the 'left' pointer one step to the right.
#             # This effectively shrinks the window and removes the duplicate character.
#             left += 1
            
#         # Once the 'while' loop finishes, the current window is guaranteed to be valid
#         # (i.e., it has no repeating characters).
#         # We add the new character at the 'right' pointer to our set.
#         char_set.add(s[right])
        
#         # We then calculate the length of the current valid window, which is (right - left + 1).
#         # We update 'max_len' if the current length is greater than the previous maximum.
#         max_len = max(max_len, right - left + 1)
        
#     # After the 'right' pointer has traversed the entire string, 'max_len' holds the answer.
#     return max_len

# Let's trace with an example: s = "abcabcbb"
# 1. right = 0, s[0] = 'a'. char_set = {'a'}, max_len = 1.
# 2. right = 1, s[1] = 'b'. char_set = {'a', 'b'}, max_len = 2.
# 3. right = 2, s[2] = 'c'. char_set = {'a', 'b', 'c'}, max_len = 3.
# 4. right = 3, s[3] = 'a'. 'a' is in char_set!
#    - while loop starts. remove 'a', left=1. char_set = {'b', 'c'}.
#    - now s[3] ('a') is not in char_set. loop ends.
#    - add 'a'. char_set = {'b', 'c', 'a'}. max_len = max(3, 3 - 1 + 1) = 3.
# 5. right = 4, s[4] = 'b'. 'b' is in char_set!
#    - while loop starts. remove 'b', left=2. char_set = {'c', 'a'}.
#    - now s[4] ('b') is not in char_set. loop ends.
#    - add 'b'. char_set = {'c', 'a', 'b'}. max_len = max(3, 4 - 2 + 1) = 3.
# ...and so on. The final answer will be 3.



# using hashmap instead of hashset
# def lengthOfLongestSubstring_map(s: str) -> int:
#     left = 0
#     max_length = 0
#     char_map = {}  # Stores character: index

#     for right, char in enumerate(s):
#         # If the character is in the map and its last seen index is within the current window
#         if char in char_map and char_map[char] >= left:
#             # Jump the left pointer past the last occurrence of the duplicate
#             left = char_map[char] + 1
        
#         # Update the character's last seen index
#         char_map[char] = right
        
#         # Update the maximum length
#         max_length = max(max_length, right - left + 1)
        
#     return max_length




