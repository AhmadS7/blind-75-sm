
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


