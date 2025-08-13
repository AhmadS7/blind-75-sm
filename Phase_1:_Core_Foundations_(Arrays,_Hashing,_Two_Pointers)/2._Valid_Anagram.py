class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         sset = {}
#         tset = {}

#         for i in s:
#             sset[i] = 1 + sset.get(i, 0)
#         for i in t:
#             tset[i] = 1 + tset.get(i, 0)
#         return sset == tset

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         start = ord('a')
#         end = ord('z')
    
#         for i in range(start, end+1):
#             if s.count(chr(i)) != t.count(chr(i)):
#                 return False
#         return True
