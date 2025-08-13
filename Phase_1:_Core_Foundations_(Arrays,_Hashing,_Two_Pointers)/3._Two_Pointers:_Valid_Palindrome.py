class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        r = 0
        l = len(s) - 1

        while r < l:
            # Move `r` pointer past non-alphanumeric characters
            if not s[r].isalnum():
                r += 1
                continue
            
            # Move `l` pointer past non-alphanumeric characters
            if not s[l].isalnum():
                l -= 1
                continue
            
            # Compare the characters, ignoring case
            if s[r].lower() != s[l].lower():
                return False
            
            # Move both pointers inward
            r += 1
            l -= 1
            
        return True

# def isPalindrome(s):
#     s = ''.join(c.lower() for c in s if c.isalnum())
#     return s == s[::-1]


# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub(r"[^a-zA-Z0-9]", "", s)
        
#         left, right = 0, len(s)-1

#         while left <= right:
#             if s[left] != s[right]:
#                 return False
            
#             left += 1
#             right -= 1
        
#         return True


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # Initialize two pointers, one at the beginning (l) and one at the end (r) of the string.
#         l, r = 0, len(s) - 1

#         # The loop continues as long as the left pointer is less than the right pointer.
#         # This ensures we are always comparing characters from opposite ends of the string.
#         while l < r:
#             # Move the left pointer to the right until it finds an alphanumeric character.
#             # We also check 'l < r' inside the nested loop to prevent the pointers from crossing.
#             while l < r and not s[l].isalnum():
#                 l += 1

#             # Move the right pointer to the left until it finds an alphanumeric character.
#             # This also includes 'l < r' to prevent crossing.
#             while l < r and not s[r].isalnum():
#                 r -= 1

#             # Compare the characters at the left and right pointers.
#             # We convert both characters to lowercase to perform a case-insensitive comparison.
#             if s[l].lower() != s[r].lower():
#                 # If the characters don't match, the string is not a palindrome.
#                 return False

#             # If the characters match, move both pointers inward to continue the comparison.
#             l += 1
#             r -= 1

#         # If the loop completes without finding any non-matching characters,
#         # it means the string is a valid palindrome.
#         return True
